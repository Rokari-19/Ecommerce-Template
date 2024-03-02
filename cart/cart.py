from store.models import Headphone


class Cart():
    def __init__(self, request):
        self.session = request.session
        # for existing users
        cart = self.session.get('session_key')

        # for new users
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # making it work on all pages of app
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # checking to see if item in cart

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()

        products = Headphone.objects.filter(id__in = product_ids)

        return products

