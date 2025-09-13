from django.shortcuts import render, HttpResponse
from .models  import Product
from .models import OrderItem
# Create your views here.
def home(request):
    # return HttpResponse("HELLO")
    # Fetch products
    products = Product.objects.all()
    print(products)
    context = {
        'products': products,

    }
    return render(request, 'home.html',context)


def cart(request):
    orderitem = OrderItem.objects.all()
    context = {
        'order_items': orderitems,

    }
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)