from django.db import models

# Create your models here.

class Question(models.Model):
  username = models.ForeignKey('User', on_delete = models.SET_NULL, null=True)
  question = models.CharField(max_length=200)
  answer = models.CharField(max_length=100)

  def __str__(self):
    return self.question

  def get_absolute_url(self):
    return reverse('question-detail', args=[str(self.id)])
