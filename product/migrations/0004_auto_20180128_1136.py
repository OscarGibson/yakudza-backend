# Generated by Django 2.0.1 on 2018-01-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180128_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kkal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
