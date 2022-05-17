import imp
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Apartment

def index(request):
    apartments = Apartment.objects.all()
    context = {
        'apartments':apartments
    }
    return render(request, 'apartments/list.html', context)

def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk = apartment_id)
    context = {
        'apartment': apartment
    }
    return render(request, 'apartments/detail.html', context)

def search(request):
    return render(request, 'apartments/search.html')
