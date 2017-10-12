from metal.models.MasterData import Supplier_Service


class SupplierServiceRepository(object):

    def get_supplier_service_by_parent(self, parent_id):
        querySet = Supplier_Service.objects.filter(Parent_Service__Id__exact=parent_id)
        # print(querySet)
        #result = querySet.values('Id', 'Service_Name', 'Parent_Service__Id')
        # print(result)
        return querySet

    def get_supplier_service_all(self):
        querySet = Supplier_Service.objects.filter(Status__exact=1)
        # print(querySet)
        #result = querySet.values('Id', 'Service_Name')
        # print(result)
        return querySet