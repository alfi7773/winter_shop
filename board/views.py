from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
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
    if request.user.is_authenticated:
            return redirect('/')

    form = LoginForm()
    if request.method == 'POST':
            form = LoginForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                # user = User.objects.filter(username=username).first()
                # if user and user.check_password(password):
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)

                    return redirect('workspace')

                # messages.error(request, 'The user is not found or the password is incorrect.')

    return render(request, 'auth/login.html', {'form': form})

def register_user(request):
    if request.user.is_authenticated:
            return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('workspace')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})

# def main2(request):
#     return render(request, 'base2.html')
# Create your views here.
