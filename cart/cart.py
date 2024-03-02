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

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # checking to see if item in cart

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()

        products = Headphone.objects.filter(id__in = product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        cart = self.cart
        cart[product_id] = product_qty

        self.session.modified = True
        n_cart = self.cart
        return n_cart
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

