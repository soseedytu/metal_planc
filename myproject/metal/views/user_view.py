from django.shortcuts import render
from metal.business.services.svs_service import SupplierService
from metal.business.services.svs_tag import TagService

app_label = 'metal'


def registration_main(request):
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



