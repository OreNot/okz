from django.shortcuts import render

from skzis.forms import SkzisForm
from skzis.models import Skzis


def get_skzis(request):
    if (request.method == 'POST'):
        form = SkzisForm(request.POST)

        if form.is_valid():
            form_skzi = form.cleaned_data['skziserial_name']
            print(form_skzi)
            skzis = Skzis.objects.all()
            all_skzis = []
            if form_skzi == '0':
                for skzi in skzis:
                    skzi_info = {
                         'id': skzi.id,
                         'skziuser_name': skzi.skziuser_name,
                         'skziserial_name': skzi.skziserial_name,
                         'pvmserial_name': skzi.pvmserial_name,
                         'pechat_number': skzi.pechat_number,
                         'adress': skzi.adress,
                         'szz': skzi.szz,
                         'catalognumber': skzi.catalognumber,
                         'description': skzi.description,
                         'sertificate': skzi.sertificate,
                         'skzi_type': skzi.skzi_type.type_name,
                         'ais': skzi.ais.ais_name,
                         'software': skzi.software.software_name,
                         'organization': skzi.organization
                    }
                    all_skzis.append(skzi_info)

                context = {'all_skzis': all_skzis, 'form': form}

                return render(request, 'skzis/skzis.html', context)

            for skzi in skzis:
                if (str.upper(str(form_skzi)) in str.upper(skzi.organization.organization_name)) or  (str.upper(str(form_skzi)) in str.upper(skzi.skziuser_name)) or (str.upper(str(form_skzi)) in str.upper(skzi.skziserial_name)) or (str.upper(str(form_skzi)) in str.upper(skzi.pvmserial_name)) or (str.upper(str(form_skzi)) in str.upper(skzi.pechat_number)) or (str.upper(str(form_skzi)) in str.upper(skzi.adress)) or (str.upper(str(form_skzi)) in str.upper(skzi.szz)) or (str.upper(str(form_skzi)) in str.upper(skzi.catalognumber)) or (str.upper(str(form_skzi)) in str.upper(skzi.description)) or (str.upper(str(form_skzi)) in str.upper(skzi.sertificate)) or (str.upper(str(form_skzi)) in str.upper(skzi.skzi_type.type_name)) or (str.upper(str(form_skzi)) in str.upper(skzi.ais.ais_name)) or (str.upper(str(form_skzi)) in str.upper(skzi.software.software_name)) :
                    skzi_info = {
                         'id': skzi.id,
                         'skziuser_name': skzi.skziuser_name,
                         'skziserial_name': skzi.skziserial_name,
                         'pvmserial_name': skzi.pvmserial_name,
                         'pechat_number': skzi.pechat_number,
                         'adress': skzi.adress,
                         'szz': skzi.szz,
                         'catalognumber': skzi.catalognumber,
                         'description': skzi.description,
                         'sertificate': skzi.sertificate,
                         'skzi_type': skzi.skzi_type.type_name,
                         'ais': skzi.ais.ais_name,
                         'software': skzi.software.software_name,
                         'organization': skzi.organization

                    }
                    all_skzis.append(skzi_info)
            context = {'all_skzis': all_skzis, 'form': form}

            return render(request, 'skzis/skzis.html', context)

    form = SkzisForm()

    skzis = Skzis.objects.all()
    all_skzis = []

    for skzi in skzis:
        skzi_info = {
            'id': skzi.id,
            'skziuser_name': skzi.skziuser_name,
            'skziserial_name': skzi.skziserial_name,
            'pvmserial_name': skzi.pvmserial_name,
            'pechat_number': skzi.pechat_number,
            'adress': skzi.adress,
            'szz': skzi.szz,
            'catalognumber': skzi.catalognumber,
            'description': skzi.description,
            'sertificate': skzi.sertificate,
            'skzi_type': skzi.skzi_type.type_name,
            'ais': skzi.ais.ais_name,
            'software': skzi.software.software_name,
            'organization': skzi.organization
        }
        all_skzis.append(skzi_info)

    context = {'all_skzis': all_skzis, 'form': form}

    return render(request, 'skzis/skzis.html', context)



