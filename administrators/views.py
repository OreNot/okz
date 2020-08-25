from django.shortcuts import render

# Create your views here.

from administrators.forms import AdministratorsForm

from administrators.models import DLNames

from administrators.models import Order_admin_ib

from administrators.models import Administrators


def get_administrators(request):

    if (request.method == 'POST'):
        form = AdministratorsForm(request.POST)

        if form.is_valid():
            adminFilter = form.cleaned_data['organization_name']
            print(adminFilter)
            #administrators = Administrators.objects.all()
            orders = Order_admin_ib.objects.all()
            all_administrators = []
            all_orders = []

            if adminFilter == '0':

                for order in orders:
                    administrator_info = {
                        'id': order.id,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file,
                            'admin_organization': order.order_organization.organization_name,
                            'fio': order.order_administrator.fio,
                            'email': order.order_administrator.e_mail,
                            'work_telephone': order.order_administrator.work_telephone,
                            'mobile_telephone': order.order_administrator.mobile_telephone,
                            'services': order.order_organization.services,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file

                    }
                    all_administrators.append(administrator_info)

                context = {'all_administrators': all_administrators, 'form': form}

                return render(request, 'administrators/administrators.html', context)
            else:
                for order in orders:
                    if (adminFilter in order.order_administrator.fio) or (adminFilter in order.order_administrator.e_mail) or (adminFilter in order.order_administrator.city) or (adminFilter in order.order_administrator.filial_name) or (adminFilter in order.order_organization.organization_name) or (adminFilter in str(order.order_organization.gid)) or (adminFilter in str(order.order_organization.inn))  or (adminFilter in order.order_organization.services):
                         administrator_info = {
                            'id': order.id,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file,
                            'admin_organization': order.order_organization.organization_name,
                            'fio': order.order_administrator.fio,
                            'email': order.order_administrator.e_mail,
                            'work_telephone': order.order_administrator.work_telephone,
                            'mobile_telephone': order.order_administrator.mobile_telephone,
                            'services': order.order_organization.services,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file

                        }
                         all_administrators.append(administrator_info)
                context = {'all_administrators': all_administrators, 'form': form}

                return render(request, 'administrators/administrators.html', context)






    form = AdministratorsForm()

    orders = Order_admin_ib.objects.all()

    all_administrators = []


    for order in orders:
        administrator_info = {
            'id': order.id,
            'order_num': order.order_num,
            'order_date': order.order_date,
            'order_file': order.order_file,
            'admin_organization': order.order_organization.organization_name,
            'fio': order.order_administrator.fio,
            'email': order.order_administrator.e_mail,
            'work_telephone': order.order_administrator.work_telephone,
            'mobile_telephone': order.order_administrator.mobile_telephone,
            'services': order.order_organization.services,
            'order_num': order.order_num,
            'order_date': order.order_date,
            'order_file': order.order_file

        }
        all_administrators.append(administrator_info)

    context = {'all_administrators': all_administrators, 'form': form}

    return render(request, 'administrators/administrators.html', context)

