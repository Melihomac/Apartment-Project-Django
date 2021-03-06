# Generated by Django 4.0.4 on 2022-05-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_alter_apartment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.CharField(max_length=15, null=True, verbose_name='Apartment Location'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Apartment Price'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ImageField(max_length=30, upload_to='', verbose_name='Apartment Image'),
        ),
    ]
