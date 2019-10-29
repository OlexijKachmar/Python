from django.db.models import TextField
from django.forms import CharField, Form, PasswordInput
from django import forms
from . import models


class CreateArticle(Form):
    title = CharField(
        label='Заголовок',
        max_length=100,
        error_messages={'required': 'Вкажіть заголовок статті'}
    )
    text = CharField(
        widget=forms.Textarea,
        max_length = 2000,
        error_messages={'required': 'Введіть текст статті'}
    )


class LoginForm(Form):
    login = CharField(
        label='Логін',
        max_length=100,
        error_messages={'required': 'Вкажіть логін'})
    password = CharField(
        label='Пароль',
        widget=PasswordInput(),
        error_messages={'required': 'Вкажіть пароль'})


class RegistrationForm(LoginForm):
    password_again = CharField(
        label='Пароль (ще раз)',
        widget=PasswordInput(),
        error_messages={'required': 'Вкажіть пароль ще раз'})

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Паролі повинні співпадати!')
        return self.cleaned_data
