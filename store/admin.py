from django.contrib import admin
from .models import Headphone, HeadphoneType
# Register your models here.
admin.site.register(HeadphoneType)
admin.site.register(Headphone)