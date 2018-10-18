from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):

    identifier = models.CharField(max_length=40, unique=True)
    user_knapsack = models.ForeignKey('Knapsack', on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD='identifier'


class Knapsack(models.Model):

    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    tools = models.ManyToManyField('Tool')
    theme = 'DEFAULT' # TODO: implement themes

class Tool(models.Model):

    identifier = models.CharField(max_length=40, unique=True)
    path = models.CharField(max_length=40)
    description = models.TextField()
