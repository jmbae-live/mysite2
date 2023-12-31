# Generated by Django 4.2.3 on 2023-08-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0007_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('posts', models.ManyToManyField(related_name='products', to='blog.post')),
            ],
        ),
    ]
