from metal.models.MasterData import Company


class CompanyRepository(object):


    def get_company_by_uen(self, company_uen):
        querySet = Company.objects.filter(Uen__exact=company_uen)

        if(querySet.count() > 0):
            return querySet.first()
        else:
            return None


    def create_company(self, company_info):
        company = Company(
            Uen=company_info['company_uen'],
            Name=company_info['company_name'],
            Address="",
            Domain="",
            Reg_No="",
            Contact_No=company_info['contact_number'],
            Unique_Code=""

        )
        company.save()
        return company