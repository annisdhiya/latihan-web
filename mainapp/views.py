from .models import *
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    a= 5*2*10
    return HttpResponse(a)

def second_page(request):
    return HttpResponse("Hello, world! Nama saya Annis")

def example(request):
    return render(request, 'example.html')  
    
def shop(request):
    return render(request, 'shop.html')

def firstpage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def am(request):
    return render(request, 'am.html')

def shop_laptop(request):
    return render(request, 'shop_laptop.html')

def shop_list(request):
    #try:
        category_laptop = Category.objects.get(pk=1)
        product_laptop = Product.objects.filter(category=category_laptop)
        return render(request, 'shop_list.html', {'product_list': product_laptop})   
    #except:
    #   return HttpResponse("Terjadi Error")
    