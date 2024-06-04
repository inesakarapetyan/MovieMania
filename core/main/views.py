from django.shortcuts import render, redirect
from .models import Logo,Category, Movie, Cart

# Create your views here.

def index(request):
    logo = Logo.objects.first()
    category_list = Category.objects.all()
    cart_items = Cart.objects.all()
    return render(request, 'main/index.html', context={
        'logo':logo,
        'category_list':category_list,
        'cart_items':cart_items
    })



def movies(request, id):
    logo = Logo.objects.first()
    movies_list = Category.objects.filter(pk=id)
    cart_items = Cart.objects.all()
    return render(request, 'main/movies.html', context={
        'logo':logo,
        'movies_list':movies_list,
        'cart_items':cart_items
    })

def cart(request):
    logo = Logo.objects.first()
    cart_items = Cart.objects.all()
    return render(request, 'main/cart.html', context={
        'logo':logo,
        'cart_items':cart_items
    })


def add_to_cart(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        cart_item = Movie.objects.get(id=movie_id)
        Cart.objects.create(movie=cart_item)
        return redirect('index')


def delete_from_cart(request):
    if request.method == 'POST':
        cart_items_id = request.POST.get('cart_items_id')
        Cart.objects.get(id=cart_items_id).delete()
        return redirect('cart')