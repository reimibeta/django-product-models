# Generated by Django 3.1.7 on 2021-03-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_builds', '0006_auto_20210311_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbuildstock',
            name='build',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_build_stock', to='product_builds.productbuild'),
        ),
    ]