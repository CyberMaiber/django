# Generated by Django 3.2.22 on 2023-10-17 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometask2_app', '0002_remove_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='GoodOne',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]