# Generated by Django 3.1.3 on 2020-12-26 13:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20201226_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 28, 13, 2, 19, 822622, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=6, verbose_name='пол'),
        ),
    ]
