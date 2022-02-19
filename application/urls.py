from email.mime import application
from django.contrib import admin
from django.urls import path
from . import views as application_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', application_views.home,name="home"),
    path('pcod/', application_views.pcod,name="pcod"),
    path('aub/', application_views.aub,name="aub"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', application_views.RegisterView.as_view(), name='register'),
]