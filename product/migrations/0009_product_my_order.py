# Generated by Django 2.0.1 on 2018-06-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20180517_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]