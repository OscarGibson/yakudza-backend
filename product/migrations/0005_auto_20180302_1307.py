# Generated by Django 2.0.1 on 2018-03-02 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180128_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='kkal',
            new_name='pieces',
        ),
    ]