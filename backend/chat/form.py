from django import forms
from .models import Person
from django.core.exceptions import NON_FIELD_ERRORS

# формируем форму моделей, на некоторые модели может быть несколько форм, если этого требует ситуация

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['login', 'password', 'name']

        error_messages = {
            'login': {
                'required': 'Обязательное поле',
                'invalid': 'Пользователь с таким логином уже существует'

            },
            'password': {
                'required': 'Обязательное поле'
            },
            NON_FIELD_ERRORS: {
                'login': 'Пользователь с таким логином уже существует',
            }
        }

        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form_input'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form_input'}),
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form_input'}),
        }


