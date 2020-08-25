from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from administrators import views

from administrators.models import Administrators, Order_admin_ib

urlpatterns = [
path('', views.get_administrators),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Order_admin_ib, template_name="administrators/administrator.html"))
]
