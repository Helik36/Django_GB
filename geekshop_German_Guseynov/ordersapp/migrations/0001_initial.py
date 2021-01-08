# Generated by Django 3.1.3 on 2021-01-08 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0005_product_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('FM', 'Формирвуется'), ('STP', 'отправлено в обработку'), ('PRD', 'обработано'), ('PD', 'оплачено'), ('RDY', 'готово к выдаче'), ('CNC', 'отменено')], default='FM', max_length=3, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания заказа')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='дата обновления заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='продукт')),
            ],
        ),
    ]
