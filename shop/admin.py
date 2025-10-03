from django.contrib import admin
from shop.models.products import Category, Product

admin.site.register([Category, Product])
