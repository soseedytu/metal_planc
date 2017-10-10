from django.db import models
from metal.models.Codes import CCodeTable
from django.contrib.auth.models import User

class MDocumentNumber(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45)
    Prefix = models.CharField(max_length=45)
    Suffix = models.CharField(max_length=45)
    Format = models.CharField(max_length=45)
    RunningNumber = models.IntegerField(null=False)

    def __str__(self):
        return self.Id

class MCompany(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Name = models.CharField(max_length=45, null=False)
    Address = models.CharField(max_length=200, null=False)
    Domain = models.CharField(max_length=45, null=False)
    RegNo = models.CharField(max_length=45, null=False)
    Code = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Name

class MUser(models.Model):
    Id = models.AutoField(primary_key=True)
    #EmailAddress = models.CharField(max_length=55, null=False, db_index=True)
    #Password = models.CharField(max_length=45, null=False)
    #Username = models.CharField(max_length=45, null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    CUserType = models.ForeignKey(CCodeTable, db_index=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False, default="admin")
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False, default=1000001)
    RfqCount = models.IntegerField(default=0)
    QuoteCount = models.IntegerField(default=0)
    Version = models.DateTimeField(null=True)
    Title = models.CharField(max_length=5)
    ContactNumber = models.CharField(max_length=45)
    MCompany_Id = models.ForeignKey(MCompany, db_index=True, null=True)

    def check_password(self, raw_password):
        # TODO: Make this auto update using
        # check_passwords setter argument
        return check_password(raw_password, self.password)

class MBuyer(models.Model):
    MUser_Id = models.OneToOneField(MUser, primary_key=True, db_index=True)
    RfqCount = models.IntegerField(default=0)
    TotalClosedRfqCount = models.IntegerField(default=0)
    TotalWithdrawRfqCount = models.IntegerField(default=0)
    TotalAwardRfqCount = models.IntegerField(default=0)

class MSupplier(models.Model):
    MUser_Id = models.OneToOneField(MUser, primary_key=True, db_index=True)
    MServiceTags = models.CharField(max_length=400)
    TotalSubmittedQuotes = models.IntegerField(default=0)
    TotalQuotesWon = models.IntegerField(default=0)
    TotalQuotesMissed = models.IntegerField(default=0)


class MServices(models.Model):
    Id = models.AutoField(primary_key=True) # system will add automatically
    MParentServices_Id = models.ForeignKey('self', db_index=True)
    ServiceName = models.CharField(max_length=45, null=False, unique=True, db_index=True)
    CMetalType = models.ForeignKey(CCodeTable, db_index=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    CommonShapeImage = models.BinaryField()

    def __str__(self):
        return self.ServiceName


class MDSupplierServices(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MServices_Id = models.ForeignKey(MServices, db_index=True)
    MCompany_Id = models.ForeignKey(MCompany, db_index=True)


class MDServiceParameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    ParameterName = models.CharField(max_length=45, null=True)
    ParameterDefaultValues = models.CharField(max_length=15, null=True)
    MServices_Id = models.ForeignKey(MServices, db_index=True)
    Uom = models.CharField(max_length=10, null=True)
    Status = models.IntegerField(null=True)
    Version = models.DateTimeField(null=True)


class MDUserRating(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MUser_Id = models.ForeignKey(MUser, null=False, db_index=True)
    UserRating = models.IntegerField(null=False)
    Comment = models.CharField(max_length=200)
    MUserRatingCol = models.CharField(max_length=45, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    Version = models.DateTimeField(null=True)


class MDSupplierServiceParameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MDSupplierServices_Id = models.ForeignKey(MDSupplierServices, db_index=True)
    ParameterName = models.CharField(max_length=45, null=True)
    MinValue = models.CharField(max_length=45, null=True)
    MaxValue = models.CharField(max_length=45, null=True)
    Uom = models.CharField(max_length=45, null=True)