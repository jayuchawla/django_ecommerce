# Generated by Django 4.2 on 2023-04-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_name_category_slug_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]