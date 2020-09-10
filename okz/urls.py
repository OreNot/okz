"""okz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^operators/', include('operators.urls')),
    url(r'^skzis/', include('skzis.urls')),
    url(r'^operatoranswers/', include('operatoranswers.urls')),
    url(r'^administrators/', include('administrators.urls')),
    url(r'^orders/', include('orders.urls')),
    #url(r'^administrators/organizations', include('administrators.urls')),
    url(r'^instructions/', include('instructions.urls')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^news/', include('news.urls')),
    url(r'', include('mainapp.urls')),
    ]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]