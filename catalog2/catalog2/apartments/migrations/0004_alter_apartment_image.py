# Generated by Django 4.0.4 on 2022-05-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_alter_apartment_description_alter_apartment_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ImageField(max_length=15, upload_to='', verbose_name='Apartment Image'),
        ),
    ]
