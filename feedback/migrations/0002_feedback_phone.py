# Generated by Django 2.0.1 on 2018-02-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
