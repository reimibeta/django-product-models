# Generated by Django 3.1.7 on 2021-05-24 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcurrency_productprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
