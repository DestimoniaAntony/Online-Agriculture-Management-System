# Generated by Django 4.2.1 on 2023-05-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_app', '0006_fertilizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]