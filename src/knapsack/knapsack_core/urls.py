from django.urls import path
from knapsack_core import views

urlpatterns = [
  path('', views.index, name='index'),
]
