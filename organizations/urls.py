from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from organizations import views
from administrators.models import Order_admin_ib, Organizations

urlpatterns = [
path('', views.get_organizations),

    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Organizations, template_name="organizations/organization.html"))
    url(r'^(?P<pk>\d+)$', views.get_organization)
]