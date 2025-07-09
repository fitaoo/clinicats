from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin, StackedInline
from .models import Anuncio, Empleado, Departamento, Perfil

# --- Admin para Anuncios ---


@admin.register(Anuncio)
class AnuncioAdmin(ModelAdmin):
    list_display = ('titulo', 'publicado', 'activo')
    list_filter = ('activo', 'publicado')
    search_fields = ('titulo',)
    exclude = ('autor',)
    readonly_fields = ('publicado',)

    fieldsets = (
        ("📝 Detalles del anuncio", {
            "fields": (("titulo", "activo"), "contenido", "imagen"),
            "classes": ("wide",),
        }),
        ("📌 Información de publicación", {
            "fields": ("publicado",),
            "classes": ("collapse",),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


# --- Admin para Empleados ---
@admin.register(Empleado)
class EmpleadoAdmin(ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('nombre', 'correo')


# --- Admin para Departamento ---
@admin.register(Departamento)
class DepartamentoAdmin(ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


# --- Inline visual para Perfil de usuario ---
class PerfilInline(StackedInline):
    model = Perfil
    can_delete = False
    fields = ['avatar']
    verbose_name_plural = 'Perfil'


# --- Admin personalizado para User con Inline de Perfil ---
class UsuarioConPerfilAdmin(UserAdmin):
    inlines = [PerfilInline]


admin.site.unregister(User)
admin.site.register(User, UsuarioConPerfilAdmin)
