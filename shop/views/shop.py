from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from shop.models import Category, Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .cart import Cart

def dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart = Cart(request)

    data = {
        "categories": categories,
        "products": products,
        "cart_count": cart.get_count()
        }

    return render(request, 'shop/index.html', context=data)

def detail(request):
    return render(request, 'shop/detail.html')

def shopping(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    cart = Cart(request)

    page = request.GET.get('page')

    page_products = paginator.get_page(page)

    return render(request, 'shop/shop.html', context={"products": page_products, "cart_count": cart.get_count()})