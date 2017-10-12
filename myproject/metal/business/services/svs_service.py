from metal.business.repository.repo_services import SupplierServiceRepository


class SupplierService(object):

    def get_supplier_service_by_parent(self, service_id):
        repo = SupplierServiceRepository()
        querySet = repo.get_supplier_service_by_parent(service_id)
        result = querySet.values('Id', 'Service_Name')
        return result;


    def get_supplier_service_all(self):
        repo = SupplierServiceRepository()
        querySet = repo.get_supplier_service_all()
        result = querySet.values('Id', 'Service_Name')
        return result;