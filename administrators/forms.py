from django import forms

from django.forms import ModelForm, TextInput, ChoiceField

from administrators.models import Organizations


class AdministratorsForm(ModelForm):

    class Meta:
        model = Organizations
        fields = ['organization_name']
        widgets = {'organization_name': TextInput(attrs={
            'class': 'form-control',
            'name': 'organization',
            'id': 'organization',
            'placeholder': 'Поиск'
        })}