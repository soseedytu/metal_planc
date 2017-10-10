from django.db import models

class CCodeCategory(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45)
    Description = models.CharField(max_length=200)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)

    def __str__(self):
        return self.Name

class CCodeTable(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45, null=False)
    Description = models.CharField(max_length=45, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    CCodeCategory_Id = models.ForeignKey(CCodeCategory, db_index=True)
    CParentCode_Id = models.ForeignKey('self', db_index=True, null=True, blank=True)
    Version = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Description


class CTags(models.Model):
    Id = models.AutoField(primary_key=True) # system will add automatically
    TagName = models.CharField(max_length=45, db_index=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)

    def __str__(self):
        return self.TagName