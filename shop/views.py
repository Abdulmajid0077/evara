from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from shop.models import Category, Product
from django.contrib.auth.models import User

def dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    data = {"categories": categories, "products": products}

    return render(request, 'shop/index.html', context=data)

def detail(request):
    return render(request, 'shop/detail.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, "shop/login.html")

def register_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if full_name and email and username and password and confirm_password:
            if password == confirm_password:
                user = User(first_name=full_name, email=email, username=username)
                user.set_password(password)
                user.save()
                return redirect('login_user')
            else:
                print("Parol notogri")
        else:
            print("Bo'sh joylarni to'ldiring")

    return render(request, "shop/login-register.html")


def logout_user(request):
    logout(request)
    return redirect('dashboard')

