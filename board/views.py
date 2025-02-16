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
    
    
def category(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    # countries = Country.objects.all()
    # cities = City.objects.all()
    # categories = Category.objects.all()
    # types = Type.objects.all()
    # brands = Brand.objects.all()
    # products = Product.objects.all()
    return render(request, 'element_category.html', {
        'category': category,
        # 'categories': categories,
        # 'countries': countries,
        # 'types': types,
        # 'brands': brands,
        'id':id,
        'products': products
    })
    
def type(request,  id):
    type = get_object_or_404(Type, id=id)
    products = Product.objects.filter(type=type)
    
    return render(request, 'type_element.html', {
        'type': type,
        'products': products,
    })
def login_user(request):
    return render(request, 'auth/index.html')

# def main2(request):
#     return render(request, 'base2.html')
# Create your views here.
