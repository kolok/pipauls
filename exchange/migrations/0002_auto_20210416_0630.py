# Generated by Django 3.1.7 on 2021-04-16 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('can_edit_product', 'create or update a product'),)},
        ),
    ]