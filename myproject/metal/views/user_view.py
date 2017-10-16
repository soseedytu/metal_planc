import json

from django.http import HttpResponse
from django.shortcuts import render
from metal.business.viewmodels.vm_registration_form import RegistrationForm
from metal.business.services.svs_service import SupplierService
from metal.business.services.svs_tag import TagService

app_label = 'metal'


def registration_main(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        reg_result = 'success'
        errors = ''

        if(form.is_valid() == False):
            reg_result = 'failed'
            errors = form.errors

        print(form.cleaned_data)
        print(form.is_valid())

        reg_result = {
            'result': reg_result,
            'errors': errors
        }
        return HttpResponse(json.dumps(reg_result), content_type="application/json")
    else:
        sup_svs = SupplierService()
        tag_svs = TagService()
        root_services = sup_svs.get_supplier_service_by_parent(None)
        tags = tag_svs.get_tags_all()
        parameters = {
            'root_services': root_services,
            'tags': tags
        }
        print(parameters)
        return render(request, 'register/index.html', parameters)



