# Generated by Django 2.0.1 on 2018-01-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='AddManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('add', models.ManyToManyField(to='product.Add')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='category.Category')),
                ('tags', models.ManyToManyField(to='tag.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('product', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
