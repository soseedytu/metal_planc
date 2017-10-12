from django.shortcuts import render
from metal.business.repository.repo_services import SupplierServiceRepository

app_label = 'metal'


def registration_main(request):
    repo = SupplierServiceRepository()
    root_services = repo.get_supplier_service_by_parent(None)
    parameters = {
        'root_services': root_services
    }
    print(parameters)
    return render(request, 'register/index.html', parameters)



