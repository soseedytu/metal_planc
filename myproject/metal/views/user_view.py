from django.shortcuts import render
from metal.business.services.svs_service import SupplierService

app_label = 'metal'


def registration_main(request):
    svs = SupplierService()
    root_services = svs.get_supplier_service_by_parent(None)
    parameters = {
        'root_services': root_services
    }
    print(parameters)
    return render(request, 'register/index.html', parameters)



