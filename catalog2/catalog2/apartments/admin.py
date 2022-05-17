from django.contrib import admin
from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'isPublished', 'location')
    list_display_links = ('id', 'name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_field = ('name')
    list_per_page = 10

admin.site.register(Apartment, ApartmentAdmin)
