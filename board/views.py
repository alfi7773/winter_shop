from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
# from django.http.response import HttpResponce

def main(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    
    text = '<h1>hello</h1>'
    return render(request, 'index.html', {
        'categories': categories,
        'countries': countries,
        'types': types,
        'brands': brands,
        'products': products
    })
    
    
def detail (request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {
        'product': product,
    })


# def main2(request):
#     return render(request, 'base2.html')
# Create your views here.
