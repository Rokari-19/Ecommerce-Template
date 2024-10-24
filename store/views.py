from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Product
from cart.cart import Cart

def store(request):
    items = Product.objects.all()
    return render(request, 'store/store.html', {
        'items':items
    })

def detail(request ,pk):
    cart = Cart(request)
    cart_items = cart.get_prods
    item = get_object_or_404(Product, pk=pk)
    related_items = Product.objects.filter(htype = item.htype).exclude(pk=pk)[0:2]
    return render(request, 'store/itemdetail.html', {
        'product':item,
        'similar':related_items,
        'cart_items':cart_items
    })

@login_required

def delete(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    item.delete()

    return redirect('homepage:index')