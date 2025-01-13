from django.contrib import admin
from .models import Galery

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)