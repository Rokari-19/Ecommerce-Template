from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('store/', views.store, name='store')
]