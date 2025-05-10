from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("HELLO")
    return render(request, 'home.html')


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)