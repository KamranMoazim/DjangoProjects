# Generated by Django 3.0.8 on 2020-08-23 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200823_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcategory',
            new_name='sub_category',
        ),
    ]
