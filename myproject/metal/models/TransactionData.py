from django.db import models
from django.contrib.auth.models import update_last_login, user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from metal.models.MasterData import User_Profile
from metal.models.Codes import Code_Table


class Document(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Title = models.CharField(max_length=45, null=False)
    Document_Type = models.ForeignKey(Code_Table, db_index=True, related_name='Document_Type')
    Short_Description = models.CharField(max_length=45)
    Long_Description = models.CharField(max_length=500)
    Submission_Date = models.DateTimeField()
    Quotation_Status = models.ForeignKey(Code_Table, db_index=True, related_name='Quotation_Status')
    Rfq_Status = models.ForeignKey(Code_Table, db_index=True, related_name='Request_For_Quotation_Status')
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False, default="admin")
    Modified_Date = models.DateTimeField(auto_now_add=True, null=False)
    Modified_By = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    User_Profile = models.ForeignKey(User_Profile, db_index=True)
    Document_No = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Title

class Request_For_Quotation(models.Model):
    Document_Id = models.OneToOneField(Document, db_index=True, primary_key=True)
    Title = models.CharField(max_length=300, null=False)
    Final_Closing_Date = models.DateTimeField()
    First_Closing_Date = models.DateTimeField()
    Revised_Closing_Date1 = models.DateTimeField()
    Revised_Closing_Date2 = models.DateTimeField()
    Total_Submitted_Quotes = models.IntegerField(default=0)
    Required_Service_Tags = models.CharField(max_length=400)
    Is_Selected = models.BooleanField(default=1)

    def __str__(self):
        return self.Title

class Supplier_Quotation(models.Model):
    Quotation_Document = models.OneToOneField(Document, db_index=True, primary_key=True, related_name='Document')
    Rfq_Document = models.ForeignKey(Document, db_index=True, related_name='Request_For_Quotation')
    Quoted_Figure = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    Valid_To_Date = models.DateTimeField()
    Revision_No = models.IntegerField()


class Document_Required_Service(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Service_Name = models.CharField(max_length=45)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False, default="admin")
    Modified_Date = models.DateTimeField(auto_now_add=True, null=False)
    Modified_By = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    Rfq_Document = models.ForeignKey(Document, db_index=True)


class Document_File_Attachment(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Document = models.ForeignKey(Document, db_index=True)
    FileName = models.CharField(max_length=150, null=False)
    FileBinary = models.BinaryField(null=False)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False, default="admin")
    Modified_Date = models.DateTimeField(auto_now_add=True, null=False)
    Modified_By = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)


class Document_Clarification(models.Model):
    Id = models.AutoField(primary_key=True, null=False)  # system will add automatically
    ClarificationQuestion = models.CharField(max_length=400, null=True)
    ClarificationAnswer = models.CharField(max_length=400, null=True)
    User_Profile = models.ForeignKey(User_Profile, db_index=True)
    Document = models.ForeignKey(Document, db_index=True)
    Version = models.DateTimeField(null=True)


class Document_Required_Service_Parameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Document_Required_Services = models.ForeignKey(Document_Required_Service, null=False, db_index=True)
    Parameter_Name = models.CharField(max_length=45, null=True)
    Parameter_Value = models.CharField(max_length=45, null=True)


class Document_Targeted_Supplier(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Document = models.ForeignKey(Document, db_index=True, null=False)
    User_Profile = models.ForeignKey(User_Profile, db_index=True, null=False)
