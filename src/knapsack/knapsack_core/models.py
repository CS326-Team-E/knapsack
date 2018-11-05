import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):

    identifier = models.CharField(max_length=40, unique=True)
    user_knapsack = models.ForeignKey(
        'Knapsack', on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = 'identifier'

    class Meta:
        ordering = ["identifier"]


class Knapsack(models.Model):

    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    tools = models.ManyToManyField('Tool')
    theme = 'DEFAULT'  # TODO: implement themes

    def __str__(self):
        return str(self.owner) + "'s knapsack"

    class Meta:
        ordering = ["owner"]


class Tool(models.Model):

    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     help_text="Unique ID for this tool",
    # )

    identifier = models.CharField(max_length=40, unique=True)
    path = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.identifier

    class Meta:
        ordering = ["identifier"]


class Question(models.Model):
    username = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=70)
    answer = models.CharField(max_length=40)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    class Meta:
        ordering = ["username"]


class ToolRequest(models.Model):
    username = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    request = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    class Meta:
        ordering = ["title"]


class ToolVote(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    request = models.ForeignKey('ToolRequest', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username) + ' votes for ' + str(self.request)

    class Meta:
        unique_together = ('username', 'request',)
