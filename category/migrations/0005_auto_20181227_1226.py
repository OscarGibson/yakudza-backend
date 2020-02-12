# Generated by Django 2.0.1 on 2018-12-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category_my_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=128),
        ),
    ]