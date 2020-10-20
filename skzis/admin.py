from django.contrib import admin

# Register your models here.

# Register your models here.
from skzis.models import SkziType, Ais, Software, Skzis

admin.site.register(SkziType)
admin.site.register(Ais)
admin.site.register(Software)
admin.site.register(Skzis)
