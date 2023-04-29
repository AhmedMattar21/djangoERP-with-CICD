# Generated by Django 4.2 on 2023-04-16 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_specs_products_fk_specs_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='fk_size_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.sizes'),
        ),
    ]
