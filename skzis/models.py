from django.db import models
from administrators.models import Organizations

class SkziType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name

class Ais(models.Model):
    ais_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ais_name

class Software(models.Model):
    software_name = models.CharField(max_length=255)

    def __str__(self):
        return self.software_name

class Skzis(models.Model):
    skziuser_name = models.CharField(max_length=512, blank=True, null=True)
    skziserial_name = models.CharField(max_length=255, blank=True, null=True)
    pvmserial_name = models.CharField(max_length=255, blank=True, null=True)
    pechat_number = models.CharField(max_length=255, blank=True, null=True)
    adress = models.CharField(max_length=1024, blank=True, null=True)
    szz = models.CharField(max_length=255, blank=True, null=True)
    catalognumber = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    sertificate = models.CharField(max_length=255, blank=True, null=True)
    skzi_type = models.ForeignKey(SkziType, on_delete=models.CASCADE)
    ais = models.ForeignKey(Ais, on_delete=models.CASCADE)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    def __str__(self):
        return self.skziserial_name
