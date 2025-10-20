from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from shop.models import Category, Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from shop.forms import LoginForm, RegisterForm


def product_with_category(request, category_id):

    products = Product.objects.filter(category_id=category_id)


    return render(request, 'shop/category-products.html', context={"products": products})

@login_required
def profile_user(request):
    return render(request, 'shop/accounts.html')

def login_user(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            
        else:
            data = {
                "form": form
            }
            return render(request, "shop/login.html", context=data)
        
    form = LoginForm()
    data = {
        "form": form
    }

    return render(request, "shop/login.html", context=data)

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.set_password(password)

            user.save()
            return redirect('login_user')
        else:
            data = {
                "form": form
            }
            return render(request, "shop/login-register.html", context=data)
    
    form = RegisterForm()

    return render(request, "shop/login-register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect('dashboard')

