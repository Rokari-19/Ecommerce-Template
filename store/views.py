from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Headphone

def store(request):
    items = Headphone.objects.all()
    return render(request, 'store/store.html', {
        'items':items
    })
