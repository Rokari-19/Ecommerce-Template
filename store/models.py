from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        ordering = ('name',)
    
    def __str__(self) -> str:
        return self.name
    


class Product(models.Model):
    htype = models.ForeignKey(ProductType, related_name = 'items', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    specs = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)


    def __str__(self) -> str:
        return self.name

