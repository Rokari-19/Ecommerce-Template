from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Headphone

def store(request):
    items = Headphone.objects.all()
    return render(request, 'store/store.html', {
        'items':items
    })

def detail(request ,pk):
    item = get_object_or_404(Headphone, pk=pk)
    related_items = Headphone.objects.filter(htype = item.htype).exclude(pk=pk)[0:2]
    return render(request, 'store/itemdetail.html', {
        'product':item,
        'similar':related_items
    })

@login_required

def delete(request, pk):
    item = get_object_or_404(Headphone, pk=pk, created_by=request.user)
    item.delete()

    return redirect('homepage:index')