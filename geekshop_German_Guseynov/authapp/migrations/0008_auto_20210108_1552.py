# Generated by Django 3.1.3 on 2021-01-08 12:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20201226_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 10, 12, 52, 14, 497894, tzinfo=utc)),
        ),
    ]
