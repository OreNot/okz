from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from news import views
from news.models import News


urlpatterns = [
    path('', ListView.as_view(queryset=News.objects.all().order_by("-publication_date")[:20],
                                template_name="news/news.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=News, template_name="news/new.html"))

]