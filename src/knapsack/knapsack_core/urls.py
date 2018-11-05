from django.urls import path
from knapsack_core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('request/', views.request_component, name='request'),
    path('library/', views.LibraryView.as_view(), name='library'),
]
