from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {}
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    # return HttpResponse("Index Shop")
    return render(request, 'shop/index.html', params)

def about(request):
    # return HttpResponse("About Us")
    return render(request, 'shop/about.html')

def contact(request):
    # return HttpResponse("Contact Us")
    return render(request, 'shop/contact.html')

def tracker(request):
    # return HttpResponse("Tracker Status")
    return render(request, 'shop/tracker.html')

def search(request):
    # return HttpResponse("Search")
    return render(request, 'shop/search.html')

def productview(request, myid):
    # return HttpResponse("Product View")
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    # print(product)
    return render(request, 'shop/prodview.html', {'product':product[0]})
    

def checkout(request):
    # return HttpResponse("Check Out")
    return render(request, 'shop/checkout.html')