# Generated by Django 4.1.4 on 2022-12-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('product_type', models.CharField(max_length=10)),
                ('num_of_bedrooms', models.IntegerField(max_length=1)),
                ('num_of_bathrooms', models.IntegerField(max_length=1)),
                ('about', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='Product')),
            ],
        ),
    ]
