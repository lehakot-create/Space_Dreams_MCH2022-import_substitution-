from django.contrib.postgres.fields import ArrayField
from django.db import models


class Company(models.Model):
    id_company = models.IntegerField(null=True, unique=True)
    Company = models.CharField(max_length=128)
    Direction = models.CharField(max_length=512)
    Description = models.TextField(null=True)
    Categories = ArrayField(base_field=models.CharField(max_length=128), null=True)
    Products = ArrayField(base_field=models.CharField(max_length=128), null=True)
    Status = models.CharField(max_length=128)
    INN = models.BigIntegerField(null=True)
    OGRN = models.BigIntegerField(null=True)
    KPP = models.BigIntegerField(null=True)
    Entity = models.CharField(max_length=128, null=True)
    Employ_number = models.IntegerField(null=True)
    Region = models.CharField(max_length=128, null=True)
    Locality = models.CharField(max_length=128, null=True)
    Address = models.CharField(max_length=128, null=True)
    Telephone = models.CharField(max_length=128, null=True)
    Post = models.CharField(max_length=128, null=True)
    URL = models.CharField(max_length=128, null=True)
    VK = models.CharField(max_length=128, null=True)
    Instagram = models.CharField(max_length=128, null=True)
    Facebook = models.CharField(max_length=128, null=True)
    Youtube = models.CharField(max_length=128, null=True)
    Catalogs = ArrayField(models.CharField(max_length=128, null=True))
