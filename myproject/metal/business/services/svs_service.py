from metal.business.repository.repo_services import SupplierServiceRepository


class SupplierService(object):

    def get_supplier_service_by_parent(self, service_id):
        repo = SupplierServiceRepository()
        queryset = repo.get_supplier_service_by_parent(service_id)
        result = queryset.values('Id', 'Service_Name', 'Parent_Service__Id')
        return result

    def get_supplier_service_all(self):
        repo = SupplierServiceRepository()
        queryset = repo.get_supplier_service_all()
        result = queryset.values('Id', 'Service_Name')
        return result

    def get_supplier_service_by_selected_service_array(self, selected_service_array):
        result = None

        if(selected_service_array is None):
            return result;

        service_id_array = {}
        i = 0
        for selected_service in selected_service_array:
            service_id_array[i] = selected_service["service_id"]
            i = i + 1

        repo = SupplierServiceRepository()
        result = repo.get_services_by_id_arrary(service_id_array)

        return result