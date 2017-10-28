import json, asyncio

from django.http import HttpResponse
from metal.business.services.svs_service import SupplierService

app_label = 'metal'


def get_service(request, service_id):

    print('----------------')
    print(service_id)
    print('----------------')

    svs = SupplierService()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    service_future = asyncio.Future()
    asyncio.ensure_future(svs.get_supplier_service_by_parent(service_future, service_id))
    loop.run_until_complete(service_future)
    services = service_future.result()
    loop.close()

    parameters = list(services)

    print('----------------')
    print(parameters)
    print('----------------')

    return HttpResponse(json.dumps(parameters), content_type="application/json")

