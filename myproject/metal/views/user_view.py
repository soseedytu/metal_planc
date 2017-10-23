import json, asyncio

from django.http import HttpResponse
from django.shortcuts import render
from metal.business.viewmodels.vm_registration_form import RegistrationForm
from metal.business.services.svs_service import SupplierService
from metal.business.services.svs_tag import TagService
from metal.business.services.svs_user import UserService
from metal.business.common.async_lib import AsyncLibrary

app_label = 'metal'


def registration_main(request):
    async_lib = AsyncLibrary()
    async_obj = async_lib.get_future()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        reg_result = 'success'
        errors = ''
        user_create_result = None

        if(form.is_valid() == False):
            reg_result = 'failed'
            errors = form.errors
        else:
            user_svs = UserService()
            user_details = form.cleaned_data
            user_details["user_password"] = request.POST['user_password']

            loop = async_obj["loop"]
            registration_future = async_obj["future"]
            # asyncio.ensure_future(user_svs.register_user(user_svs, registration_future))
            # loop.run_until_complete(registration_future)
            async_lib.execute_async(user_svs.register_user(registration_future, user_details), loop, registration_future)
            user_create_result = registration_future.result()
            async_lib.close_loop(loop)
            #user_create_result = user_svs.register_user(user_details)

        # print(form.cleaned_data)
        # print(form.is_valid())

        reg_result = {
            'result': reg_result,
            'errors': errors,
            'user_info': user_create_result
        }
        return HttpResponse(json.dumps(reg_result), content_type="application/json")
    else:
        sup_svs = SupplierService()
        tag_svs = TagService()

        loop = async_obj["loop"]
        service_future = async_obj["future"]
        tags_future = async_lib.get_future_from_loop(loop)

        async_lib.execute_async(sup_svs.get_supplier_service_by_parent(service_future, None), loop, service_future)
        async_lib.execute_async(tag_svs.get_tags_all(tags_future), loop, tags_future)

        # asyncio.ensure_future(sup_svs.get_supplier_service_by_parent(service_future, None))
        # loop.run_until_complete(service_future)
        # asyncio.ensure_future(tag_svs.get_tags_all(tags_future))
        # loop.run_until_complete(tags_future)

        root_services = service_future.result()
        tags = tags_future.result()
        async_lib.close_loop(loop)

        # root_services = sup_svs.get_supplier_service_by_parent(None)
        # tags = tag_svs.get_tags_all()
        parameters = {
            'root_services': root_services,
            'tags': tags
        }
        print(parameters)
        return render(request, 'register/index.html', parameters)



