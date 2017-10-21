from metal.business.repository.repo_company import CompanyRepository
from metal.business.repository.repo_user import UserRepository
from metal.business.repository.repo_code import CodeTableRepository
from metal.business.repository.repo_buyer import BuyerRepository
from metal.business.repository.repo_supplier import SupplierRepository
from metal.business.services.svs_tag import TagService
from metal.business.services.svs_service import SupplierService
from metal.business.common.constants import Constants
from metal.business.common.functions import Functions


class UserService(object):

    def register_user(self, new_user_object):
        uen = new_user_object['company_uen']
        company_repo = CompanyRepository()
        company_profile = company_repo.get_company_by_uen(uen)
        print("Company Profile")
        print(company_profile)

        user_repo = UserRepository()
        user_repo.begin_transaction()

        if(company_profile == None):
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

        if(user_profile == None):
            return 0

        ## create specific user type
        user_details = None
        if(user_type == Constants.code_usertype_buyer):

            buyer_repo = BuyerRepository()
            user_details = buyer_repo.register_buyer(user_profile)

        elif(user_type == Constants.code_usertype_supplier):

            ## collect tags
            common_func = Functions()
            tags_arrary = common_func.convert_json_string_to_dict(new_user_object['tags_text'])
            tag_svs = TagService()
            tags = tag_svs.get_tags_text_from_arrary(tags_arrary)

            ## collect services
            selected_services_arrary = common_func.convert_json_string_to_dict(new_user_object['services_text'])
            supplier_svs = SupplierService()
            selected_supplier_services = supplier_svs.get_supplier_service_by_selected_service_array(selected_services_arrary)


            ## save in supplier repository
            supplier_repo = SupplierRepository()
            user_details = supplier_repo.register_supplier(user_profile, tags)

        else:

            user_repo.rollback_transaction()
            return -1

        ## finally commit transaction
        user_repo.commit_transaction()
        new_user_object["user_id"] = user_profile.Id
        new_user_object["user_profile_id"] = user_profile.user_id
        new_user_object["user_password"] = None
        return new_user_object


