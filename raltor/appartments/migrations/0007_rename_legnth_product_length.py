# Generated by Django 4.1.3 on 2022-12-13 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appartments', '0006_product_style'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='legnth',
            new_name='length',
        ),
    ]
