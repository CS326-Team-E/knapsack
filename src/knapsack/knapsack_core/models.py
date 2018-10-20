from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):

    identifier = models.CharField(max_length=40, unique=True)
    user_knapsack = models.ForeignKey('Knapsack', on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD='identifier'


class Knapsack(models.Model):

    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    tools = models.ManyToManyField('Tool')
    theme = 'DEFAULT' # TODO: implement themes

    def __str__(self):
      return str(self.owner) + "'s knapsack"

class Tool(models.Model):

    identifier = models.CharField(max_length=40, unique=True)
    path = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
      return self.identifier

class Question(models.Model):
  username = models.ForeignKey('User', on_delete = models.SET_NULL, null=True)
  question = models.CharField(max_length=70)
  answer = models.CharField(max_length=40)

  def __str__(self):
    return self.question

  def get_absolute_url(self):
    return reverse('question-detail', args=[str(self.id)])

