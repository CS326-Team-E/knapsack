from django.urls import path
from knapsack_core import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('request/', views.request_component, name='request'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('example/', views.single_component, name='single_component'),
    path('signup', views.SignUp.as_view(), name='signup')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]