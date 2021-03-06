# Generated by Django 2.0.1 on 2018-04-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='used_promotion',
            field=models.BooleanField(default=False, verbose_name='Знижка використана'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=256, verbose_name='Емейл'),
        ),
    ]
