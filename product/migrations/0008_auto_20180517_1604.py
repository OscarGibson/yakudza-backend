# Generated by Django 2.0.1 on 2018-05-17 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20180328_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmanager',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
