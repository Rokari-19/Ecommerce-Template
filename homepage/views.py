from django.shortcuts import render, redirect
from django.contrib.auth import logout
from store.models import *

from . import forms
# Create your views here.
def index(request):
    category = HeadphoneType.objects.all()
    return render(request, 'homepage/index.html', {
        'categories': category
    })

def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = forms.SignupForm
        return render(request, 'homepage/signup.html', {
            'form':form
        })
        


def logOut(request):
    logout(request)
    return redirect('/login/')
