from django import forms

from django.forms import ModelForm, TextInput, ChoiceField

from skzis.models import Skzis


class SkzisForm(ModelForm):
    class Meta:
        model = Skzis
        fields = ['skziserial_name']
        widgets = {'skziserial_name': TextInput(attrs={
            'class': 'form-control',
            'name': 'organization',
            'id': 'organization',
            'placeholder': 'Поиск'
        })}