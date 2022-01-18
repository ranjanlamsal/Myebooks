from django.shortcuts import render
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()

    # params = {'product': products, 'no_of_slides': nSlides, 'range': range(1, n)}
    # allprods = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    for cat in categories:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        allprods.append([prod, range(1,nSlides), nSlides])
    params = {'allprods': allprods}
    return render(request,'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request,'shop/contact.html')


def search(request):
    return render(request,'shop/search.html')


def productview(request, myid):
    #fetching the product using the id
    product = Product.objects.filter(id = myid)
    return render(request,'shop/productview.html')


def checkout(request):
    return render(request,'shop/checkout.html')


def tracker(request):
    return render(request,'shop/tracker.html')

def my_cart(request):
    return render(request,'shop/mycart.html')

