# Generated by Django 2.0.1 on 2018-04-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('order', '0009_auto_20180411_2201'),
        ('order', '0008_order_total_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='simple_id',
            field=models.IntegerField(default=0),
        ),
    ]
