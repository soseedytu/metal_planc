from metal.models.MasterData import Supplier_Services_Profile
from metal.models.MasterData import Supplier_Service_Profile_Parameter
from metal.business.repository.repo_base import BaseRepository
from datetime import datetime


class SupplierServiceProfileRepository(BaseRepository):

    def create_supplier_service_profile(self, service_obj, company_obj):
        service_profile = Supplier_Services_Profile(
            Supplier_Service=service_obj,
            Company=company_obj
        )
        service_profile.save()
        return service_profile

    def create_supplier_service_profile_param(self, supplier_services_profile_obj, service_profile_param):

        # '[{
        # "service_id":"32",
        # "min_width":"12",
        # "min_height":"12",
        # "min_thickness":"12",
        # "max_width":"21",
        # "max_height":"21",
        # "max_thickness":"21"
        # }]'

        saved_params = []
        i = 0
        for key, value in service_profile_param.items():
            param = Supplier_Service_Profile_Parameter(
                Parameter_Name=key,
                Parameter_Default_Values=value,
                Supplier_Service_Profile=supplier_services_profile_obj,
                Uom='mm',
                Status=1,
                Version=datetime.now()
            )
            param.save()
            saved_params.insert(i, param)
            i = i + 1

        return saved_params

