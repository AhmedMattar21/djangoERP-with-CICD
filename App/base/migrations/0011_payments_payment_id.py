# Generated by Django 4.1.7 on 2023-04-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_payments_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_id',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
