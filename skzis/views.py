from django.shortcuts import render

# Create your views here.

from administrators.forms import AdministratorsForm

from administrators.models import DLNames

from administrators.models import Order_admin_ib

from administrators.models import Administrators


def get_skzis(request):



                return render(request, 'skzis/skzis.html')
