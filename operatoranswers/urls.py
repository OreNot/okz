from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from operatoranswers import views
from operatoranswers.models import Operatoranswers

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Operatoranswers.objects.all(),
                                template_name="operatoranswers/operatoranswers.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Operatoranswers, template_name="operatoranswers/operatoranswer.html"))

]