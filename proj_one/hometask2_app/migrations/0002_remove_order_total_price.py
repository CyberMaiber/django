# Generated by Django 3.2.22 on 2023-10-15 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometask2_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
