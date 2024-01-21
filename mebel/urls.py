from django.urls import path, include
from . import views
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('shop', views.shop, name="shop"),
    path('cart', views.cart, name="cart"),
    path('productdetails', views.productdetails, name="productdetails"),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('login', LoginView.as_view(), name="mebel_login"),
    path('logout', LogoutView.as_view(), name="mebel_logout"),
    path('signup', views.signup, name='signup'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),

]
