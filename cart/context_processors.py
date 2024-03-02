from .cart import Cart

# making cart app work on all sites using contextprocessor

def cart(request):
    return {'cart':Cart(request)}