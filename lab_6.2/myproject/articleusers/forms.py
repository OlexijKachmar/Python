from django.forms import ModelForm
from . import models
from django.forms import CharField, Form, PasswordInput
from django import forms


class CreateArticle(ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'checked']
