# Generated by Django 4.2.1 on 2023-05-31 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_app', '0005_alter_crop_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizer', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]