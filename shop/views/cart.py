from django.shortcuts import render, redirect
from django.http import JsonResponse
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = request.session.get('session_key')

        if not cart:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]+=1
        else:
            self.cart[product_id] = 1

        self.session.modified = True


def add_to_cart(request, product_id):
    cart = Cart(request)

    if Product.objects.filter(id=product_id).exists():
        pass
    if request.method == "POST":
        # Bu yerda mahsulotni foydalanuvchi savatiga qo‘shasiz
        return JsonResponse({"message": "Added successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)

    