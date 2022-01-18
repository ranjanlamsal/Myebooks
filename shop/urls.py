from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "ShopHome"),
    path('about/', views.about, name = "AboutUs"),
    path('contact/', views.contact, name = "ContactUS"),
    path('search/', views.search, name = "Search"),
    path('productview/<int:myid>', views.productview, name = "ProductView"),
    path('checkout/', views.checkout, name = "Checkout"),
    path('tracker/', views.tracker, name = "TrackingStatus"),
    path('mycart/', views.my_cart, name = "My_cart"),
]