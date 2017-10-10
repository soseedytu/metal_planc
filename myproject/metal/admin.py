from django.contrib import admin

from .models.MasterData import Document_Number
from .models.MasterData import Company
from .models.MasterData import User_Profile
from .models.MasterData import Buyer
from .models.MasterData import Supplier
from .models.MasterData import Supplier_Service
from .models.MasterData import Supplier_Services_Profile
from .models.MasterData import Supplier_Service_Profile_Parameter
from .models.MasterData import User_Profile_Rating
from .models.TransactionData import Document
from .models.TransactionData import Request_For_Quotation
from .models.TransactionData import Supplier_Quotation
from .models.TransactionData import Document_Required_Service
from .models.TransactionData import Document_File_Attachment
from .models.TransactionData import Document_Clarification
from .models.TransactionData import Document_Required_Service_Parameter
from .models.TransactionData import Document_Targeted_Supplier
from .models.Codes import Code_Category
from .models.Codes import Code_Table
from .models.Codes import Tag
from django.contrib import admin

# set View Site Link of Admin Site
admin.site.site_url = '/public_site'

#Code Category
class CodeCategoryAdmin(admin.ModelAdmin):
   date_hierarchy = 'CreatedDate'
   search_fields = ['Name', 'Description', 'Status']
   list_display = ('Id','Name', 'Description', 'CreatedDate', 'Status', 'Version')
   list_filter = ('CreatedDate',)

class CodeTableAdmin(admin.ModelAdmin):
   date_hierarchy = 'CreatedDate'
   search_fields = ['Name', 'Description', 'Status']
   list_display = ('Id','Name', 'Description', 'Code_Category', 'CreatedDate', 'Status')
   list_filter = ('CreatedDate',)

class UserProfileAdmin(admin.ModelAdmin):
   date_hierarchy = 'Created_Date'
   search_fields = ['user']
   list_display = ('Id', 'user', 'Title', 'Rfq_Count', 'Quotation_Count', 'Contact_Number', 'Company')
   list_filter = ('Created_Date',)

admin.site.register(Document_Number)
admin.site.register(Company)
admin.site.register(User_Profile, UserProfileAdmin)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Supplier_Service)
admin.site.register(Supplier_Services_Profile)
admin.site.register(Supplier_Service_Profile_Parameter)
admin.site.register(User_Profile_Rating)
admin.site.register(Document)
admin.site.register(Request_For_Quotation)
admin.site.register(Supplier_Quotation)
admin.site.register(Document_Required_Service)
admin.site.register(Document_File_Attachment)
admin.site.register(Document_Clarification)
admin.site.register(Document_Required_Service_Parameter)
admin.site.register(Document_Targeted_Supplier)
admin.site.register(Code_Category, CodeCategoryAdmin)
admin.site.register(Code_Table, CodeTableAdmin)
admin.site.register(Tag)