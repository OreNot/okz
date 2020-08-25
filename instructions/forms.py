from django.forms import ModelForm, TextInput, ChoiceField

class InstructionsForm(ModelForm):
    class Meta:
            widgets = {'email': TextInput(attrs={
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Email'
        })}
