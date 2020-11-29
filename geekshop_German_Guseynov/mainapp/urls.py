from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('product/all', mainapp.products, name='products_all'),
    path('product/home', mainapp.products, name='products_home'),
    path('product/office', mainapp.products, name='products_office'),
    path('product/modern', mainapp.products, name='products_modern'),
    path('product/classic', mainapp.products, name='products_classic'),
]