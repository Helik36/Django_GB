from django.shortcuts import render

from mainapp.models import Product, ProductCategory
# Create your views here.

def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    print(pk)
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': "Контакты"
    }
    return render(request, 'mainapp/contact.html', content)

def products_all(request):
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)

def products_home(request):
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)

def products_ofice(request):
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)

def products_modern(request):
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)

def products_classic(request):
    links_menu = [
        {'href': 'mainapp:products_all', 'name': 'все'},
        {'href': 'mainapp:products_home', 'name': 'дом'},
        {'href': 'mainapp:products_office', 'name': 'офис'},
        {'href': 'mainapp:products_modern', 'name': 'модерн'},
        {'href': 'mainapp:products_classic', 'name': 'классика'},
    ]
    content = {
        'title': "Продукты",
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)