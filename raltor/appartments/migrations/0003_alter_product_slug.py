# Generated by Django 4.1.4 on 2022-12-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartments', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]
