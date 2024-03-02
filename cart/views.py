from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Headphone
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_prods = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart/summary.html', {'cart_items':cart_prods, 'quantities':quantities})

def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Headphone, id = product_id) #getting product
        cart.add(product=product, quantity = product_qty) #saving to cart
        # getting cart quantity
        cart_quantity = cart.__len__()
        response = JsonResponse({
            'qty':cart_quantity
            })

        return response



def delete_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        
        
        response = JsonResponse({'product':product_id})
        return response



def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response
