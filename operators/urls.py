from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from operators import views
from operators.models import Operators

urlpatterns = [

   # url(r'^$', ListView.as_view(queryset=Operators.objects.all().order_by("-date")[:20],
   #                             template_name="operators/operators.html")),

    path('', views.get_operators),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Operators, template_name="operators/operator.html"))
]
