from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('addcontact/', views.addcontact, name='addcontact'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('cart/', views.cart, name='cartview'),
    path('login/', views.login, name='login'),
    path('login/user/', views.userlogin, name='userlogin'),
    path('signup/', views.signup, name='signup'),
    path('signup/user/', views.usersignup, name='usersignup'),
    
    
]
