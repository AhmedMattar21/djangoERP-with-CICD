# Generated by Django 4.2 on 2023-04-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouses',
            name='warehouse_desc',
            field=models.TextField(default='None'),
        ),
    ]
