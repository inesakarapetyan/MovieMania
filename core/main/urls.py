from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('movies/<int:id>', views.movies, name='movies'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart')

]