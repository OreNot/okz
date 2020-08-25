from django import forms

from django.forms import ModelForm, TextInput, ChoiceField

from operators.models import Filials


class OperatorsForm(ModelForm):
    class Meta:
        model = Filials
        fields = ['filial_name']
        CHOICES = (
            ('КУЦ Ангарск', 'КУЦ Ангарск'),
            ('КУЦ Владимир', 'КУЦ Владимир'),
            ('КУЦ Глазов', 'КУЦ Глазов'),
            ('КУЦ Зеленогорск', 'КУЦ Зеленогорск'),
            ('КУЦ Ковров', 'КУЦ Ковров'),
            ('КУЦ Москва', 'КУЦ Москва'),
            ('КУЦ Н. Новгород', 'КУЦ Н. Новгород'),
            ('КУЦ Новосибирск', 'КУЦ Новосибирск'),
            ('КУЦ Новоуральск', 'КУЦ Новоуральск'),
            ('КУЦ Саров', 'КУЦ Саров'),
            ('КУЦ Северск', 'КУЦ Северск'),
            ('КУЦ Спб', 'КУЦ Спб'),
            ('КУЦ Электросталь', 'КУЦ Электросталь'),
            
        )
        blank_choice = (('0', 'Филиал'),)

        widgets = {'filial_name': forms.Select(attrs={
            'class': 'form-control',
            'name': 'filialname',
            'id': 'filialname',
            'placeholder': 'Выберите филиал',
            'style': 'width:auto;',
            'onchange': 'toggleSelect(this)'
        }, choices=blank_choice + CHOICES)}
