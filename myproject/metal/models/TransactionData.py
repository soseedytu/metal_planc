from django.db import models
from django.contrib.auth.models import update_last_login, user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from metal.models.MasterData import MUser
from metal.models.Codes import CCodeTable


class TDocument(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Title = models.CharField(max_length=45, null=False)
    CDocumentType = models.ForeignKey(CCodeTable, db_index=True, related_name='Document_Type')
    ShortDescription = models.CharField(max_length=45)
    LongDescription = models.CharField(max_length=500)
    SubmissionDate = models.DateTimeField()
    CQuotationStatus = models.ForeignKey(CCodeTable, db_index=True, related_name='Quotation_Status')
    CRfqStatus = models.ForeignKey(CCodeTable, db_index=True, related_name='Request_For_Quotation_Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    MUser_Id = models.ForeignKey(MUser, db_index=True)
    DocumentNo = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Title

class TRequestForQuotation(models.Model):
    Document_Id = models.OneToOneField(TDocument, db_index=True, primary_key=True)
    Title = models.CharField(max_length=300, null=False)
    FinalClosingDate = models.DateTimeField()
    FirstClosingDate = models.DateTimeField()
    RevisedClosingDate1 = models.DateTimeField()
    RevisedClosingDate2 = models.DateTimeField()
    TotalSubmittedQuotes = models.IntegerField(default=0)
    RequiredServiceTags = models.CharField(max_length=400)
    IsSelected = models.BooleanField(default=1)

    def __str__(self):
        return self.Title

class TSupplierQuotation(models.Model):
    Document_Id = models.OneToOneField(TDocument, db_index=True, primary_key=True, related_name='Document_ID')
    TRfq_Id = models.ForeignKey(TDocument, db_index=True, related_name='Request_For_Quotation_ID')
    QuotedFigure = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    ValidToDate = models.DateTimeField()
    RevisionNo = models.IntegerField()


class TDRequiredServices(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MService_Name = models.CharField(max_length=45)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    TRfq_Id = models.ForeignKey(TDocument, db_index=True)


class TFileAttachments(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDocument_Id = models.ForeignKey(TDocument, db_index=True)
    FileName = models.CharField(max_length=150, null=False)
    FileBinary = models.BinaryField(null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)


class TClarifications(models.Model):
    Id = models.AutoField(primary_key=True, null=False)  # system will add automatically
    ClarificationQuestion = models.CharField(max_length=400, null=True)
    ClarificationAnswer = models.CharField(max_length=400, null=True)
    MAskingPerson_Id = models.ForeignKey(MUser, db_index=True)
    TDocument_Id = models.ForeignKey(TDocument, db_index=True)
    Version = models.DateTimeField(null=True)


class TDRequiredServicesParameters(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDRequiredServices_Id = models.ForeignKey(TDRequiredServices, null=False, db_index=True)
    ParameterName = models.CharField(max_length=45, null=True)
    ParameterValue = models.CharField(max_length=45, null=True)
    TDRequiredServicesParametersCol = models.CharField(max_length=45, null=True)


class TTargetedSuppliers(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDocument_Id = models.ForeignKey(TDocument, db_index=True, null=False)
    MUser_Id = models.ForeignKey(MUser, db_index=True, null=False)
