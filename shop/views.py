from django.shortcuts import render


def index(request):
    return render(request,'shop/index.html')


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return render(request,'shop/contact.htmm')


def search(request):
    return render(request,'shop/search.html')


def productview(request):
    return render(request,'shop/productview.html')


def checkout(request):
    return render(request,'shop/checkout.html')


def tracker(request):
    return render(request,'shop/tracker.html')

