from django.shortcuts import render

# Create your views here.

from administrators.forms import AdministratorsForm

from administrators.models import DLNames

from administrators.models import Order_admin_ib

from administrators.models import Administrators
from orders.forms import OrdersForm

def get_order(request, pk):
    print(pk)
    order = Order_admin_ib.objects.get(pk=pk)
    print(order.order_organization.organization_name)

    order_info = {
        'id': order.id,
        'order_num': order.order_num,
        'order_date': order.order_date,
        'order_file': order.order_file,
        'order_organization': order.order_organization,
        'fio': order.order_administrator.fio,
        'email': order.order_administrator.e_mail,
        'work_telephone': order.order_administrator.work_telephone,
        'mobile_telephone': order.order_administrator.mobile_telephone,
        'services': order.order_organization.services,

    }



    context = {'order_info': order_info}


    return render(request,  'orders/order.html', context)



def get_orders(request):

    if (request.method == 'POST'):
        form = AdministratorsForm(request.POST)

        if form.is_valid():
            orderFilter = form.cleaned_data['organization_name']
            print(orderFilter)

            form = OrdersForm()

            orders = Order_admin_ib.objects.all()

            all_orders = []

            if orderFilter == '0':

                    for order in orders:
                        order_info = {
                            'id': order.id,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file,
                            'order_organization': order.order_organization,
                            'fio': order.order_administrator.fio,
                            'email': order.order_administrator.e_mail,
                            'work_telephone': order.order_administrator.work_telephone,
                            'mobile_telephone': order.order_administrator.mobile_telephone,
                            'services': order.order_organization.services,

                        }
                        all_orders.append(order_info)

                    context = {'all_orders': all_orders, 'form': form}

                    return render(request, 'orders/orders.html', context)
            else:
                for order in orders:
                    print(str.upper(str(orderFilter)))
                    print(str.upper(order.order_organization.organization_name))
                    if (str.upper(str(orderFilter)) in str.upper(str(order.order_num))) or (str(str.upper(orderFilter)) in str.upper(order.order_date)) or (str.upper(str(orderFilter)) in str.upper(order.order_organization.organization_name)) or (str.upper(str(orderFilter)) in str.upper(order.order_organization.full_organization_name)):
                        order_info = {
                            'id': order.id,
                            'order_num': order.order_num,
                            'order_date': order.order_date,
                            'order_file': order.order_file,
                            'order_organization': order.order_organization,
                            'fio': order.order_administrator.fio,
                            'email': order.order_administrator.e_mail,
                            'work_telephone': order.order_administrator.work_telephone,
                            'mobile_telephone': order.order_administrator.mobile_telephone,
                            'services': order.order_organization.services,

                        }
                        all_orders.append(order_info)

                context = {'all_orders': all_orders, 'form': form}

                return render(request, 'orders/orders.html', context)



    form = OrdersForm()

    orders = Order_admin_ib.objects.all()

    all_orders = []


    for order in orders:
        order_info = {
            'id': order.id,
            'order_num': order.order_num,
            'order_date': order.order_date,
            'order_file': order.order_file,
            'order_organization': order.order_organization,
            'fio': order.order_administrator.fio,
            'email': order.order_administrator.e_mail,
            'work_telephone': order.order_administrator.work_telephone,
            'mobile_telephone': order.order_administrator.mobile_telephone,
            'services': order.order_organization.services,

        }
        all_orders.append(order_info)

    context = {'all_orders': all_orders, 'form': form}

    return render(request, 'orders/orders.html', context)

