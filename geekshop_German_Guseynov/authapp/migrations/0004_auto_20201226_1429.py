# Generated by Django 3.1.3 on 2020-12-26 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20201223_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 28, 11, 29, 43, 634649, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(default=18, verbose_name='возвраст'),
        ),
    ]
