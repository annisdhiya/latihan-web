from django.urls import path
from . import views 
urlpatterns = [
    path('shop/laptop/', views.shop_laptop),
    path('shop/list/', views.shop_list),
    path('am/', views.am),
    path('secondpage/', views.secondpage),
    path('firstpage/', views.firstpage),
    path('shop/', views.shop),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landing_page),
]