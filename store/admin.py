from django.contrib import admin
from .models import ProductType, Product
# Register your models here.
admin.site.register(ProductType)
admin.site.register(Product)