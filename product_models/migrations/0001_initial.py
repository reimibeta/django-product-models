# Generated by Django 3.1.7 on 2021-06-02 04:44

import datetime_utils.date_time
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=30)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterialSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSizeFormatSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_models.productsizeformatset')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='product_models.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_models.productcurrency')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_price', to='product_models.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_models.product')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_part', to='product_models.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_models.productmaterialset')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_material', to='product_models.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/products/')),
                ('thumbnail', models.ImageField(blank=True, editable=False, null=True, upload_to='images/products/thumbnails/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product_models.product')),
            ],
        ),
    ]
