from django.urls import path
from shop.views import dashboard, login_user, logout_user, register_user, profile_user, shopping, product_with_category, add_to_cart

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name="logout_user"),
    path('register/', register_user, name='register_user'),
    path('profile/', profile_user, name='profile_user'),
    path('shop/', shopping, name='shopping'),
    path('category/<int:category_id>/', product_with_category, name='category'),
    path('cart/<int:category_id>/', add_to_cart)
]