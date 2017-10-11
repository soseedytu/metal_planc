from django.db import models
from metal.models.Codes import Code_Table
from django.contrib.auth.models import User


class Document_Number(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45)
    Prefix = models.CharField(max_length=45)
    Suffix = models.CharField(max_length=45)
    Format = models.CharField(max_length=45)
    RunningNumber = models.IntegerField(null=False)

    def __str__(self):
        return self.Id


class Company(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Name = models.CharField(max_length=45, null=False)
    Address = models.CharField(max_length=200, null=False)
    Domain = models.CharField(max_length=45, null=False)
    Reg_No = models.CharField(max_length=45, null=False)
    Unique_Code = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Name


class User_Profile(models.Model):
    Id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User_Type = models.ForeignKey(Code_Table, db_index=False)
    Rfq_Count = models.IntegerField(default=0)
    Quotation_Count = models.IntegerField(default=0)
    Version = models.DateTimeField(null=True)
    Title = models.CharField(max_length=5)
    Contact_Number = models.CharField(max_length=45)
    Company = models.ForeignKey(Company, db_index=True, null=True)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False, default="admin")
    Modified_Date = models.DateTimeField(auto_now_add=True, null=False)
    Modified_By = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.user.username


class Buyer(models.Model):
    User_Profile = models.OneToOneField(User_Profile, primary_key=True, db_index=True)
    Rfq_Count = models.IntegerField(default=0)
    Total_Closed_Rfq_Count = models.IntegerField(default=0)
    Total_Withdraw_Rfq_Count = models.IntegerField(default=0)
    Total_Award_Rfq_Count = models.IntegerField(default=0)

    def __str__(self):
        return self.User_Profile.user.username


class Supplier(models.Model):
    User_Profile = models.OneToOneField(User_Profile, primary_key=True, db_index=True)
    MServiceTags = models.CharField(max_length=400)
    Total_SubmittedQuotes = models.IntegerField(default=0)
    Total_QuotesWon = models.IntegerField(default=0)
    Total_QuotesMissed = models.IntegerField(default=0)

    def __str__(self):
        return self.User_Profile.user.username


class Supplier_Service(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Parent_Services = models.ForeignKey('self', db_index=True)
    Service_Name = models.CharField(max_length=45, null=False, unique=True, db_index=True)
    Metal_Type = models.ForeignKey(Code_Table, db_index=True)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False, default="admin")
    Modified_Date = models.DateTimeField(auto_now_add=True, null=False)
    Modified_By = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    Common_Shape_Image = models.BinaryField()

    def __str__(self):
        return self.ServiceName


class Supplier_Services_Profile(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Supplier_Service = models.ForeignKey(Supplier_Service, db_index=True)
    Company = models.ForeignKey(Company, db_index=True)


class Supplier_Service_Profile_Parameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Parameter_Name = models.CharField(max_length=45, null=True)
    Parameter_Default_Values = models.CharField(max_length=15, null=True)
    Supplier_Service = models.ForeignKey(Supplier_Service, db_index=True)
    Uom = models.CharField(max_length=10, null=True)
    Status = models.IntegerField(null=True)
    Version = models.DateTimeField(null=True)


class User_Profile_Rating(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    User_Profile = models.ForeignKey(User_Profile, null=False, db_index=True)
    User_Rating = models.IntegerField(null=False)
    Comment = models.CharField(max_length=200)
    Created_Date = models.DateTimeField(auto_now_add=True, null=False)
    Created_By = models.CharField(max_length=45, null=False)
    Version = models.DateTimeField(null=True)
