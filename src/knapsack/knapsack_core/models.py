from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User as BuiltinUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class User(AbstractBaseUser):

    identifier = models.CharField(max_length=40, unique=True)
    user_knapsack = models.ForeignKey(
        'Knapsack', on_delete=models.SET_NULL, null=True)
    mirrored_user = models.OneToOneField(
        BuiltinUser, on_delete=models.CASCADE)
    USERNAME_FIELD = 'identifier'

    @receiver(post_save, sender=BuiltinUser)
    def create_user_user(sender, instance, created, **kwargs):
        if created:
            User.objects.create(mirrored_user=instance, identifier=instance.username)

    @receiver(post_save, sender=BuiltinUser)
    def save_user_user(sender, instance, **kwargs):
        instance.user.save()

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
    html = models.TextField(default='Component missing')
    location_x = models.FloatField(default=42.389)
    location_y = models.FloatField(default=-72.529)
    description = models.TextField(null=True)

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
