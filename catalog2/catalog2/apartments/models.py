from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=30, verbose_name='Apartment Name')
    description = models.TextField(max_length=1000, verbose_name='Apartment Description')
    image = models.ImageField(max_length=30, verbose_name='Apartment Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creating Date')
    isPublished = models.BooleanField(default=True)
    location = models.CharField(max_length=15, null=True, verbose_name='Apartment Location')
    price = models.CharField(max_length=15, null=True, verbose_name='Apartment Price')
    square_meters = models.CharField(max_length=15, null=True, verbose_name='How Many Square Meters')
    apartment_number = models.CharField(max_length=15, null=True, verbose_name='Apartment Number')
    color = models.CharField(max_length=15, null=True, verbose_name='Apartment Color')
    
    def __str__(self):
        return self.name
    
    def get_image_path(self):
        return '/img/'+ self.image.name
