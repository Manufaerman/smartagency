from django.contrib import admin
from .models import servicio

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'created', 'updated']
    search_fields = ['id', 'nombre']
    readonly_fields = ('created','updated')

admin.site.register(servicio, ServiciosAdmin)