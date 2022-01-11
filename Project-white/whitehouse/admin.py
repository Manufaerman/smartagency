from django.contrib import admin
from .models import Clientes, Vivienda, reservas, Categorias

class ClientesAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "apellido2"]
    search_fields = ["id", "nombre",]

admin.site.register(Clientes, ClientesAdmin)

class ViviendaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "direccion", "descripcion", "precio"]
    search_fields = ["id", "nombre", "direccion", "descripcion"]

admin.site.register(Vivienda, ViviendaAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categorias, CategoriaAdmin)

class reservasAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','fecha_salida')
    list_filter = ['fecha_salida','status']

    
admin.site.register(reservas, reservasAdmin)