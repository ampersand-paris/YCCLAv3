# Generated by Django 4.1.1 on 2022-09-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_delete_productadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='primary_color',
            field=models.CharField(default='var(--main-blue)', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_color',
            field=models.CharField(default='var(--main-red)', max_length=100),
        ),
    ]
