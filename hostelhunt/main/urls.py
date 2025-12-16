from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('find/', views.find, name='find'),
    path('list/', views.list_hostel, name='list'),
    path('contact/', views.contact, name='contact'),
    path('sorry/', views.sorry, name='sorry'),
     path('contact/', views.contact, name='contact'),
]
