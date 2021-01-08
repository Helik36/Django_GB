
import json, os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

from authapp.models import ShopUser, ShopUserProfile

from mainapp.models import Location



class Command(BaseCommand):

    def handle(self, *args, **options):
      users = ShopUser.objects.all()
      for user in users:
          user_profile = ShopUserProfile.objects.create(user=user)
          user_profile.save()