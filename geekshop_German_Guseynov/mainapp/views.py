import random

from django.conf import settings
import os
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from mainapp.models import Product, ProductCategory

from basketapp.models import Basket

from mainapp.models import Location


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []

def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]

def get_same_product(hot_product):
    return Product.objects.filter(category__pk=hot_product.category.pk).exclude(pk=hot_product.pk)[:3]

def main(request):
    title = 'Главная'

    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None, page=1):
    print(pk)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=category.pk)

        paginator = Paginator(products_list, 2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)

        content = {
            'title' : title,
            'links_menu': links_menu,
            'products': product_paginator,
            'category': category,
            'basket': get_basket(request.user),
            'hot_product': get_hot_product()
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_product((hot_product))

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': get_basket(request.user),
        'hot_product': hot_product
    }

    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = [
        {"city": "Москва",
         "phone": "+7-888-888-8888",
         "email": "info@geekshop.ru",
         "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations, 'basket': get_basket(request.user),}
    return render(request, "mainapp/contact.html", content)

# def contact(request):
#     title = 'контакты'
#
#     locations = Location.objects.all()
#
#     content = {
#         'title' : title,
#         'locations': locations,
#     }
#
#     return render(request, "mainapp/contact.html", content)