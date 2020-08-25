from django.shortcuts import render
# Create your views here.

from administrators.models import Order_admin_ib, Organizations
from organizations.forms import OrganizationsForm


def get_organization(request, pk):
    print(pk)
    organization = Organizations.objects.get(pk=pk)
    print(Organizations.organization_name)
    orders = Order_admin_ib.objects.filter(order_organization=pk)

    organization_info = {
        'id': organization.id,
            'organization_name': organization.organization_name,
            'gid': organization.gid,
            'inn': organization.inn,
            'organization_orders': orders
    }

    context = {'organization_info': organization_info}


    return render(request,  'organizations/organization.html', context)

def get_organizations(request):
    if (request.method == 'POST'):
        form = OrganizationsForm(request.POST)

        if form.is_valid():
            organization_name = form.cleaned_data['organization_name']
            print(organization_name)
            organizations = Organizations.objects.all()
            all_organizations = []
            gids = []
            orders = Order_admin_ib.objects.all()
            if organization_name == '0':
                for organization in organizations:
                    organizationOrderList = []

                    for order in orders:
                        if organization.id == order.order_organization:
                            organizationOrderList.append(order)

                    organization_info = {
                        'id': organization.id,
                        'organization_name': organization.organization_name,
                        'gid': organization.gid,
                        'organization_orders': organizationOrderList

                    }
                    if (organization.gid not in gids):
                        gids.append(organization.gid)
                        all_organizations.append(organization_info)


                context = {'all_organizations': all_organizations, 'form': form}

                return render(request, 'organizations/organizations.html', context)

            print(len(organizations))
            for organization in organizations:

                if (str.upper(str(organization_name)) in str.upper(organization.organization_name)) or (str.upper(str(organization_name)) in str.upper(organization.inn)) or (organization_name ==organization.gid):
                    print(organization.gid)
                    print(str.upper(str(organization_name)))

                    print(str.upper(organization.organization_name))
                    organizationOrderList = []
                    for order in orders:
                        if organization.id == order.order_organization:
                            organizationOrderList.append(order)

                    organization_info = {
                        'id': organization.id,
                        'organization_name': organization.organization_name,
                        'gid': organization.gid,


                    }
                    if (organization.gid not in gids):
                        gids.append(organization.gid)
                        all_organizations.append(organization_info)

                    print(len(all_organizations))
                    for i in all_organizations:
                        print(i)
                    context = {'all_organizations': all_organizations, 'form': form}

                    return render(request, 'organizations/organizations.html', context)

    form = OrganizationsForm()

    orders = Order_admin_ib.objects.all()
    organizations = Organizations.objects.all()

    all_organizations = []
    gids = []

    for organization in organizations:
        organizationOrderList = []
        for order in orders:
            if organization.id == order.order_organization:
                organizationOrderList.append(order)

        organization_info = {
            'id': organization.id,
            'organization_name': organization.organization_name,
            'gid': organization.gid,
            'organization_orders': organizationOrderList


        }
        if(organization.gid not in gids):
            gids.append(organization.gid)
            all_organizations.append(organization_info)

    context = {'all_organizations': all_organizations, 'form': form}

    return render(request, 'organizations/organizations.html', context)
