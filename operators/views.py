from django.shortcuts import render
from .forms import OperatorsForm
from operators.models import Operators
from django.http import HttpResponse

def get_operators(request):


    if(request.method == 'POST'):
        form = OperatorsForm(request.POST)

        if form.is_valid():
            filial_name = form.cleaned_data['filial_name']
            print(filial_name)
            operators = Operators.objects.all()
            all_operators = []
            if filial_name == '0':
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
                if filial_name in operator.filial.rg_kuc_hpsm:
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


