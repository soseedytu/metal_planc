import json

from django.http import HttpResponse
from metal.business.services.svs_service import SupplierService

app_label = 'metal'


def get_service(request, service_id):

    print('----------------')
    print(service_id)
    print('----------------')

    svs = SupplierService()
    services = svs.get_supplier_service_by_parent(service_id)
    parameters = list(services)
    print('----------------')
    print(parameters)
    print('----------------')
    return HttpResponse(json.dumps(parameters), content_type="application/json")

