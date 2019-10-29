from django.db import models


# Create your models here.
class Article():
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    checked = models.BooleanField()


class User():
    username = models.TextField()
    password = models.TextField()
    articles = []

