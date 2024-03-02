from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_summary, name='cart_summary'),
    path('add/', views.add_cart, name='add_cart'),
    path('delete/', views.delete_cart, name='cart_delete'),
    path('update/', views.update_cart, name='cart_update')
]