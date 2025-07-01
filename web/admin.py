from django.contrib import admin
from .models import Anuncio, Empleado


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'activo')
    list_filter = ('activo', 'publicado')
    search_fields = ('titulo',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    list_filter = ('direccion',)
