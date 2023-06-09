# Generated by Django 3.2.12 on 2023-04-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_internal_id', models.TextField()),
                ('product_name', models.TextField()),
                ('product_cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_sell_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_line', models.TextField()),
                ('product_barcode', models.TextField()),
                ('product_tax_num', models.TextField()),
            ],
        ),
    ]
