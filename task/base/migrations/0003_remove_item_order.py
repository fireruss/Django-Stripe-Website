# Generated by Django 4.0.2 on 2022-11-28 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_order_item_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
    ]