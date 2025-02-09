from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# from django.http.response import HttpResponce

def main(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    
    text = '<h1>hello</h1>'
    return render(request, 'index.html', {
        'categories': categories,
        'countries': countries,
        'types': types,
        'brands': brands,
    })

# Create your views here.
