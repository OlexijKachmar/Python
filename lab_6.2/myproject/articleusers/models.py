from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import TextField
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, default="None",on_delete='PROTECT')
    checked = models.BooleanField()

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.TextField()
    password: TextField = models.TextField()

    def __str__(self):
        return self.username
#