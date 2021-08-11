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

def me(request):
    return render(request, 'me.html')