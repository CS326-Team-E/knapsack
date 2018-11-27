from django.urls import path
from knapsack_core import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('example/', views.single_component, name='single_component'),
    path('request/', views.request_component, name='request'),
    path('request/vote/<int:request_id>', views.vote_component, name='vote'),
    path('request/new', views.new_component, name='new'),
    path('request/remove/<int:request_id>', views.remove_component, name='remove'),

    path('signup', views.SignUp.as_view(), name='signup')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]