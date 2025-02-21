from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .filter import ProductFilter

from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.sessions.models import Session


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart 
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = [
        {'product': product, 'quantity': cart[str(product.id)]}
        for product in products
    ]

    return render(request, 'cart.html', {'cart_items': cart_items})


def main(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    categories2 = AtCategory.objects.all()
    
    text = '<h1>hello</h1>'
    return render(request, 'index.html', {
        'categories': categories,
        'countries': countries,
        'types': types,
        'brands': brands,
        'products': products,
        'categories2': categories2,
    })
    
    

def catalogue(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    categories2 = AtCategory.objects.all()

    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)

    filter_set = ProductFilter(data=request.GET, queryset=products)
    products = filter_set.qs

    try:
        page_size = int(request.GET.get('limit', 6))
    except ValueError:
        page_size = 6
    page = int(request.GET.get('page', 1))

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)

    return render(request, 'catalogue.html', {
        'categories': categories,
        'countries': countries,
        'types': types,
        'brands': brands,
        'products': products,
        'categories2': categories2,
        'filter': filter_set,
    })


    
def detail (request, id):
    product = get_object_or_404(Product, id=id)
    products = Product.objects.all()
    category = get_object_or_404(Category, id=id)
    # productss = Product.objects.filter(category=category)
    categories = Category.objects.all()
    types = Type.objects.all()
    categories2 = AtCategory.objects.all()
    return render(request, 'detail.html', {
        'product': product,
        'products': products,
        'category': category,
        'id':id,
        # 'products': productss,
        'categories': categories,
        'types': types,
        'categories2': categories2,
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
    
    
def at_category(request, id):
    at_category = get_object_or_404(AtCategory, id=id)
    products = Product.objects.filter(at_category=at_category)    
    
    return render(request, 'cat.html', {
        'products': products, 
        'cat2': at_category,
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

                    return redirect('/')

                messages.error(request, 'The user is not found or the password is incorrect.')

    return render(request, 'auth/login.html', {'form': form})

def register_user(request):
    if request.user.is_authenticated:
            return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})

def logout_user(request):
        logout(request)
        return redirect('/')
    
    
# def main2(request):
#     return render(request, 'base2.html')
# Create your views here.
