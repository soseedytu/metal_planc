import sys, asyncio

# -- Metal Class -- #
from metal.business.repository.repo_company import CompanyRepository
from metal.business.repository.repo_user import UserRepository
from metal.business.repository.repo_code import CodeTableRepository
from metal.business.repository.repo_buyer import BuyerRepository
from metal.business.repository.repo_supplier import SupplierRepository
from metal.business.repository.repo_supplier_service import SupplierServiceProfileRepository
from metal.business.services.svs_tag import TagService
from metal.business.services.svs_service import SupplierService
from metal.business.common.constants import Constants
from metal.business.common.functions import Functions
from metal.models.MasterData import User_Profile

# -- Django Contrib Class -- #
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# -- Django Core Class -- #
from django.core.exceptions import ObjectDoesNotExist

# -- Django http Class -- #
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

class UserService(object):

    async def register_user(self, future, new_user_object):
        try:
            uen = new_user_object['company_uen']
            company_repo = CompanyRepository()
            company_profile = company_repo.get_company_by_uen(uen)
            print("Company Profile")
            print(company_profile)

            user_repo = UserRepository()
            user_repo.begin_transaction()

            if (company_profile == None):
                company_profile = company_repo.create_company(new_user_object)

            user_type = Constants.code_usertype_buyer
            if (new_user_object['register_as_supplier'] == 'true'):
                user_type = Constants.code_usertype_supplier

            ## get user type code
            code_repo = CodeTableRepository()
            user_type_code = code_repo.get_code_by_code_id(user_type)

            ## create user in djang auth library
            django_user = user_repo.create_django_user(new_user_object)
            ## create user profile in our table
            user_profile = user_repo.register_user(new_user_object, user_type_code, company_profile, django_user)

            if (user_profile == None):
                future.set_result(0)

            ## create specific user type
            user_details = None
            if (user_type == Constants.code_usertype_buyer):

                buyer_repo = BuyerRepository()
                user_details = buyer_repo.register_buyer(user_profile)

            elif (user_type == Constants.code_usertype_supplier):

                ## collect tags
                common_func = Functions()
                tags_arrary = common_func.convert_json_string_to_dict(new_user_object['tags_text'])
                tag_svs = TagService()
                tags = tag_svs.get_tags_text_from_arrary(tags_arrary)

                ## collect services
                selected_services_arrary = common_func.convert_json_string_to_dict(new_user_object['services_text'])
                supplier_svs = SupplierService()
                selected_supplier_services = supplier_svs.get_supplier_service_by_selected_service_array(
                    selected_services_arrary)

                ## save supplier service profile and its parameters
                profile_repo = SupplierServiceProfileRepository()
                for service_profile in selected_supplier_services:
                    saved_serviced_profile = profile_repo.create_supplier_service_profile(service_profile, company_profile)

                    for service_param in selected_services_arrary:
                        saved_serviced_profile_param = profile_repo.create_supplier_service_profile_param(
                            saved_serviced_profile, service_param)

                ## save in supplier repository
                supplier_repo = SupplierRepository()
                user_details = supplier_repo.register_supplier(user_profile, tags)

            else:

                user_repo.rollback_transaction()
                future.set_result(-1)

            ## finally commit transaction
            user_repo.commit_transaction()
            new_user_object["user_id"] = user_profile.Id
            new_user_object["user_profile_id"] = user_profile.user_id
            new_user_object["user_password"] = None
            future.set_result(new_user_object)
            return new_user_object
        except:
            print("error: " + sys.exc_info()[0])
            raise
        # return new_user_object


    def validate_user(self, request, _email, _password):
        _value = 'public_index'
        _user = None
        try:
            user_repo = UserRepository()
            _user = user_repo.get_user(_email.lower())
        except ObjectDoesNotExist:
            username = None
            # raise  Http404("User does not exist")
            print('user does not exist')
            messages.error(request, 'You don''t have authorization. Please register first.')
            #return HttpResponseRedirect(reverse('public_index'))
            _value = 'public_index'
            # _url = 'site/index.html'
        if _user is not None:
            print(_user.username)
            user = authenticate(request, username=_user.username, password=_password)
            try:
                #user_type = User_Profile.objects.get(user=_user).User_Type
                #user_type = user_type.Name.lower()
                user_type_code = user_repo.get_user_profile(_user).User_Type.Code_Table_Code
                print(user_type_code)
            except ObjectDoesNotExist:
                print('user does not exist')
                messages.error(request, 'Insufficient authorization')
                #return HttpResponseRedirect(reverse('public_index'))
                _value = 'public_index'
            if user is not None:
                print('authenticated')
                if user.is_active:
                    print('user is active')
                    auth_login(request, user)
                    print(user_type_code)
                    print(Constants.code_usertype_supplier)
                    if str(user_type_code) == str(Constants.code_usertype_supplier):
                        print('supplier url')
                        _url = 'user_supplier/index.html'
                        #return HttpResponseRedirect(reverse('user_supplier_index'))
                        _value = 'user_supplier_index'
                        print (_value)
                        return _value
                    elif str(user_type_code) == str(Constants.code_usertype_buyer):
                        _url = 'user_buyer/index.html'
                        #return HttpResponseRedirect(reverse('user_buyer_index'))
                        # return render(request, 'buyer/Dashboard.html')
                        _value = 'user_buyer_index'
                        print(_value)
                        return _value
                else:
                    print('user is not active')
                    messages.error(request, 'Non Active User.')
                    # _url = 'site/index.html'
                    #return HttpResponseRedirect(reverse('public_index'))
                    _value = 'public_index'
            else:
                print('Invalid Username or Password.')
                # return HttpResponse('username or password wrong')
                # raise forms.ValidationError(form.fields['EmailAddress'].error_messages['Bad Username or Password'])
                messages.error(request, 'Invalid Username or Password.')
                #return HttpResponseRedirect(reverse('public_index'))
                _value = 'public_index'
        return _value