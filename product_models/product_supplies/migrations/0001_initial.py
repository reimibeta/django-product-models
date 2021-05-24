# Generated by Django 3.1.7 on 2021-03-08 13:38

import datetime_utils.date_time
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff_groups', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('wallet_models', '0003_walletwithdraw'),
        ('product_stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('request_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('supply_date', models.DateField(blank=True, null=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
            options={
                'verbose_name': 'Product supplies',
                'verbose_name_plural': 'Product supplies',
            },
        ),
        migrations.CreateModel(
            name='ProductSupplyStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('is_transferred', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_models.wallet')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_stocks.productstock')),
                ('supply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_supply_stock', to='product_supplies.productsupply')),
            ],
            options={
                'verbose_name': 'Product supply stocks',
                'verbose_name_plural': 'Product supply stocks',
            },
        ),
        migrations.CreateModel(
            name='ProductSupplyDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cost_delivery', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('delivery_date', models.DateTimeField(default=datetime_utils.date_time.DateTime.datetimenow)),
                ('arrived_date', models.DateTimeField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, choices=[('OPTIONAL', 'optional'), ('EXPIRED', 'expired'), ('REFUND', 'refund'), ('FAILED', 'failed'), ('UNPAID', 'unpaid'), ('PAID', 'paid')], max_length=120, null=True)),
                ('delivery_status', models.CharField(blank=True, choices=[('UNFULFILLED', 'unfulfilled'), ('DELIVERING', 'delivering'), ('RETURNING', 'returning'), ('ARRIVED', 'arrived'), ('COLLECTED', 'collected')], max_length=120, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_models.wallet')),
                ('deliver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_groups.staffdeliver')),
                ('supply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_supply_deliveries', to='product_supplies.productsupply')),
            ],
            options={
                'verbose_name': 'Product supply deliveries',
                'verbose_name_plural': 'Product supply deliveries',
            },
        ),
    ]