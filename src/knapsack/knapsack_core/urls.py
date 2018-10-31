from django.urls import path
from knapsack_core import views

urlpatterns = [
  path('', views.index, name='index'),
  path('map/', views.MapView.as_view(), name='map'),
]
