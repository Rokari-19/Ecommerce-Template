from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('store/', views.store, name='store'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete')
]