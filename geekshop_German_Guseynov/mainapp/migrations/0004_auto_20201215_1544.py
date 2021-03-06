# Generated by Django 3.1.3 on 2020-12-15 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Названиие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество на складе'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_desc',
            field=models.CharField(max_length=120, unique=True, verbose_name='Названиие'),
        ),
    ]
