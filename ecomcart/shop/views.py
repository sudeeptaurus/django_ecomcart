from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Get an instance of a logger
# import logging
# logger = logging.getLogger(__name__)

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
    if request.method == "POST":
        # print(request)
        name = request.POST.get('name', '')
        # print(name)
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    # return HttpResponse("Contact Us")
        return render(request, 'shop/contact.html', {'thank': thank})
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        print(request)
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                # pass
                # return HttpResponse('else')
                # return HttpResponse('error')
                return HttpResponse('{}')
        except Exception as e:
            #
            # return HttpResponse(f'exception {e}')
            # return HttpResponse('error')
            return HttpResponse('{}')
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
    return render(request, 'shop/prodview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        # print(request)
        name = request.POST.get('name', '')
        # print(name)
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        print(name, email, phone, address, city, state, zip_code)
        order = Order(items_json=items_json, name=name, email=email,
                      address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
    # return HttpResponse("Check Out")
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
