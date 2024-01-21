from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import LoginForm, User, SingUpForm, AddToCartForm
from .forms import BlogForm
from .models import Blog, Category, UserProfile, Product, Cart, CartItem


# Create your views here.


def index(request):
    context = {}
    return render(request, 'mebel/index.html', context=context)

def blog(request):
    blogs = Blog.objects.all().order_by("-published_date")
    context = {"blogs": blogs}
    return render(request, 'mebel/blog.html', context=context)

def contact(request):
    context = {}
    return render(request, 'mebel/contact.html', context=context)

def shop(request):
    context = {}
    return render(request, 'mebel/shop.html', context=context)

def cart(request):
    context = {}
    return render(request, 'mebel/cart.html', context=context)

def productdetails(request):
    context = {}
    return render(request, 'mebel/productdetails.html', context=context)




'''def account(request):
    context = {}
    return render(request, 'mebel/account.html', context=context)'''


def search(request):
    query = request.GET.get('query')
    blogs = Blog.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by("-published_date")
    context = {"blogs": blogs}
    return render(request, 'mebel/blog.html', context=context)

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_date = timezone.now()
            blog.user = request.user
            blog.save()
            return index(request)
    form = BlogForm()
    context = {"form": form}
    return render(request, 'mebel/create.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)
            return redirect('mebel/index.html')
    else:
        form = SingUpForm()
    return render(request, 'mebel/signup.html', {'form': form})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, 'mebel/cart.html', {'cart': cart})

