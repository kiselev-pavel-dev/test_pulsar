# Generated by Django 4.1.4 on 2022-12-12 15:07

import product.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=product.fields.WEBPField(
                upload_to="media", verbose_name="Изображение"
            ),
        ),
    ]