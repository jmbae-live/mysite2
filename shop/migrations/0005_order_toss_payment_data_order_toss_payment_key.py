# Generated by Django 4.2.4 on 2023-08-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='toss_payment_data',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='toss_payment_key',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
