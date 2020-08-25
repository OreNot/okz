from django.db import models


class OrderStatuses(models.Model):
    status_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.status_name

class OrderActivities(models.Model):
    activity_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.activity_name



class Organizations(models.Model):
    docid = models.IntegerField()
    gid = models.IntegerField()
    inn = models.CharField(max_length=255)
    full_organization_name = models.CharField(max_length=512)
    organization_name = models.CharField(max_length=255)
    services = models.CharField(max_length=1024)
    doc_num = models.CharField(max_length=1024)
    doc_date = models.DateTimeField(blank=True, null=True)
    order_start_date = models.DateTimeField(blank=True, null=True)
    order_end_date = models.DateTimeField(blank=True, null=True)
    order_status = models.ForeignKey(OrderStatuses, on_delete=models.CASCADE)
    order_activity = models.ForeignKey(OrderActivities, on_delete=models.CASCADE)
    document_price = models.CharField(max_length=255, blank=True, null=True)
    document_price_with_nds = models.CharField(max_length=255, blank=True, null=True)
    doc_prepare_date = models.DateTimeField(blank=True, null=True)
    doc_eosdo_date = models.DateTimeField(blank=True, null=True)
    doc_sending_date = models.DateTimeField(blank=True, null=True)
    order_activity_date = models.DateTimeField(blank=True, null=True)
    doc_eosdo_num = models.CharField(max_length=255, blank=True, null=True)
    doc_eosdo_link = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.organization_name


class DLNames(models.Model):
    dl_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dl_name

class Administrators(models.Model):

    fio = models.CharField(max_length=255)
    e_mail = models.CharField(max_length=255, null=True)
    work_telephone = models.CharField(max_length=255, null=True)
    mobile_telephone = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    filial_name = models.CharField(max_length=255, null=True)
    dl_name = models.ForeignKey(DLNames, on_delete=models.CASCADE)

    def __str__(self):
        return self.fio

class Order_admin_ib(models.Model):
    order_num = models.CharField(max_length=255, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_file = models.FileField(upload_to='mainapp/static/mainapp/admin_ib_orders', blank=True, null=True)
    order_organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    order_administrator = models.ForeignKey(Administrators, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_num
