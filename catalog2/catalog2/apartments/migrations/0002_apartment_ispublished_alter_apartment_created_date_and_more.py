# Generated by Django 4.0.4 on 2022-05-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creating Date'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Apartment Location'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Apartment Image'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Apartment Name'),
        ),
    ]