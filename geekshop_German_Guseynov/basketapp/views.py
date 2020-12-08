from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from mainapp.models import Product

from basketapp.models import Basket


def basket(request):
    pass


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user, product=product).first()
    print(basket_item)
    if not basket_item:
        basket_item = Basket(user=request.user, product=product)

    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # возвращается на тот же адрес, от куда пришёл

def delete(request, pk):
    pass
