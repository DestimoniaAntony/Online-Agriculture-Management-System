# Generated by Django 4.2.1 on 2023-06-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_app', '0013_rename_quantity_crop_total_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
