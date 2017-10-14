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
admin.site.site_url = '/public'

#Company
class CompanyAdmin(admin.ModelAdmin):
   search_fields = ['Name', 'Address', 'Domain']
   list_display = ('Id','Name', 'Address', 'Domain','Reg_No', 'Unique_Code')
   list_filter = ('Name','Domain',)

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
   list_display = ('Id', 'user', 'User_Type', 'Title','Company','Contact_Number','Rfq_Count','Quotation_Count')
   list_filter = ('Created_Date',)

class BuyerAdmin(admin.ModelAdmin):
   search_fields = ['User_Profile']
   list_display = ('User_Profile', 'Rfq_Count', 'Total_Closed_Rfq_Count','Total_Withdraw_Rfq_Count','Total_Award_Rfq_Count')
   list_filter = ('User_Profile',)

class SupplierAdmin(admin.ModelAdmin):
   search_fields = ['User_Profile']
   list_display = ('User_Profile', 'MServiceTags', 'Total_SubmittedQuotes', 'Total_QuotesWon','Total_QuotesMissed')
   list_filter = ('User_Profile',)

admin.site.register(Document_Number)
admin.site.register(Company, CompanyAdmin)
admin.site.register(User_Profile, UserProfileAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Supplier, SupplierAdmin)
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