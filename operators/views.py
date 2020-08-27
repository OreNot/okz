from django.shortcuts import render
from .forms import OperatorsForm
from operators.models import Operators
from django.http import HttpResponse

def get_operators(request):


    if(request.method == 'POST'):
        form = OperatorsForm(request.POST)

        if form.is_valid():
            fio = form.cleaned_data['fio']
            print(fio)
            operators = Operators.objects.all()
            all_operators = []
            if fio == '0':
                for operator in operators:
                            operator_info = {
                            'id': operator.id,
                            'filial_name': operator.filial.filial_name,
                            'fio': operator.fio,
                            'position': operator.position,
                            'telephone': operator.telephone,
                            'email': operator.email

                            }
                            all_operators.append(operator_info)

                context = {'all_operators': all_operators, 'form': form}

                return render(request, 'operators/operators.html', context)

            for operator in operators:
                if str.upper(str(fio)) in str.upper(operator.fio):
                     operator_info = {
                        'id': operator.id,
                        'filial_name': operator.filial.filial_name,
                        'fio': operator.fio,
                        'position': operator.position,
                        'telephone': operator.telephone,
                        'email': operator.email

                        }
                     all_operators.append(operator_info)
            context = {'all_operators': all_operators, 'form': form}

            return render(request, 'operators/operators.html', context)







    form = OperatorsForm()

    operators = Operators.objects.all()
    all_operators = []

    for operator in operators:

        operator_info = {
           'id': operator.id,
           'filial_name': operator.filial.filial_name,
           'fio': operator.fio,
           'position': operator.position,
           'telephone': operator.telephone,
           'email':  operator.email

        }
        all_operators.append(operator_info)

    context = {'all_operators': all_operators, 'form': form}

    return render(request, 'operators/operators.html', context)


