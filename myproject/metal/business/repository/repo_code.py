from metal.models.Codes import Code_Category
from metal.models.Codes import Code_Table


class CodeTableRepository(object):

    def get_code_by_code_id(self, code_id):
        querySet = Code_Table.objects.filter(Code_Table_Code__exact=code_id)
        if (querySet.count() > 0):
            return querySet.first()
        else:
            return None

    def get_codes_by_category_id(self, category_id):
        querySet = Code_Table.objects.filter(Category_Code__exact=category_id)
        return querySet