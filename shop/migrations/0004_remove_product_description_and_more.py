# Generated by Django 4.2.4 on 2023-08-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_translations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
