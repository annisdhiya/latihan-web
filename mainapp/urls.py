from django.urls import path
from . import views 
urlpatterns = [
    path('me/', views.me),
    path('secondpage/', views.secondpage),
    path('firstpage/', views.firstpage),
    path('shop/', views.shop),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landing_page),
]