from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from skzis import views
from skzis.models import Skzis

urlpatterns = [
path('', views.get_skzis),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Skzis, template_name="skzis/skzi.html"))
]