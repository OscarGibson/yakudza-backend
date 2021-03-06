# Generated by Django 2.0.1 on 2018-01-28 09:15

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                # ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id', models.UUIDField(default=uuid.uuid4, max_length=64, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('phone', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adds', models.ManyToManyField(to='product.AddManager')),
                ('product', models.ManyToManyField(to='product.ProductManager')),
            ],
        ),
    ]
