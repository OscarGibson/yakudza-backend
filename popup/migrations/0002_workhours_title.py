# Generated by Django 2.0.1 on 2019-12-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workhours',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]