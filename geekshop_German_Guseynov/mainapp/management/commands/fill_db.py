
import json, os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

from authapp.models import ShopUser

from mainapp.models import Location

JSON_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')
json_data = json.loads(open('mainapp/json/contact__locations.json', encoding='utf-8').read())



def load_json_data(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), encoding='UTF-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_json_data('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_json_data('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            Product.objects.create(**product)


        ShopUser.objects.create_superuser('django', 'django@geekbrains.local', 'geekbrains', age=22)
