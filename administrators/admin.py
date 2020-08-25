from django.contrib import admin

# Register your models here.
from administrators.models import Administrators, OrderStatuses, OrderActivities, Organizations, DLNames, Order_admin_ib

admin.site.register(Administrators)
admin.site.register(OrderStatuses)
admin.site.register(OrderActivities)
admin.site.register(Organizations)
admin.site.register(DLNames)
admin.site.register(Order_admin_ib)