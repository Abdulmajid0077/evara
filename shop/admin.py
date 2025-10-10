from django.contrib import admin
from shop.models.products import Category, Product

admin.site.register([Category, ])

class ProductAdmin(admin.ModelAdmin):
    model = Product
    exclude = ('discount_price', )
    list_display = ('name', 'price')
    search_fields = ('name', )

admin.site.register(Product, ProductAdmin)