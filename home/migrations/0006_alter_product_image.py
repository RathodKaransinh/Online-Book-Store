# Generated by Django 5.0 on 2023-12-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_category_remove_order_label_remove_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='static/'),
        ),
    ]