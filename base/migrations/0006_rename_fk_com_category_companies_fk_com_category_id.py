# Generated by Django 4.1.7 on 2023-04-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_fk_com_category_id_companies_fk_com_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='FK_com_category',
            new_name='FK_com_category_id',
        ),
    ]
