from django.db import models

class Filials(models.Model):
    filial_name = models.CharField(max_length=255, null=True)
    service_point_email = models.CharField(max_length=255, null=True)
    cn = models.CharField(max_length=255, null=True)
    rg_hpsm = models.CharField(max_length=255, null=True)
    rg_kuc_hpsm = models.CharField(max_length=255, null=True)
    ss_adress = models.TextField(null=True)
    rg_hpsm_coordinator = models.TextField(null=True)
    post_system_contact = models.TextField(null=True)
    work_problems = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.filial_name

class Operators(models.Model):
    fio = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    service_uz_name = models.CharField(max_length=255, null=True)
    dss_cert_thumbrint = models.CharField(max_length=255, null=True)
    dss_cert_valid_to = models.DateTimeField(null=True)
    filial = models.ForeignKey(Filials, on_delete=models.CASCADE)
    def __str__(self):
        return self.fio