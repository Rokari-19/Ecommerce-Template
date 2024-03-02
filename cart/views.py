from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Headphone
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_prods = cart.get_prods
    return render(request, 'cart/summary.html', {'cart_items':cart_prods})

def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Headphone, id = product_id) #getting product
        cart.add(product=product) #saving to cart
        cart_quantity = cart.__len__()
        response = JsonResponse({
            'Product Name: ':product.name,
            'qty':cart_quantity
            })

        return response



def delete_cart(request):
    pass

def update_cart(request):
    pass