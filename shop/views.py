from django.shortcuts import render, HttpResponse
from .models  import Product
# Create your views here.
def home(request):
    # return HttpResponse("HELLO")
    # Fetch products
    products = Product.objects.all()
    print(products)
    context = {
        'products': products,
        "product" : products[0]
    }
    return render(request, 'home.html',context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)