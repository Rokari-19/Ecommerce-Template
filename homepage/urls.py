from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from .forms import LoginForm
app_name = 'homepage'

urlpatterns = [
    path('', index, name= 'index'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='homepage/signin.html', authentication_form=LoginForm), name='login'),
    path('logout/', logOut, name='logout')
]
