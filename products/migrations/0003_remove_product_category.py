# Generated by Django 4.1.7 on 2023-03-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_pricice_product_price_remove_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
