from django.contrib import admin
from .models import Anuncio, Empleado
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Perfil

# --- Admin Anuncio ---


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'activo')
    list_filter = ('activo', 'publicado')
    search_fields = ('titulo',)
    exclude = ('autor',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Solo al crear, no al editar
            obj.autor = request.user
        super().save_model(request, obj, form, change)

# --- Admin Empleado ---


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    list_filter = ('direccion',)


class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    fields = ['avatar']  # 👈 Mostrar el avatar en el admin
    verbose_name_plural = 'Perfil'


class UsuarioConPerfilAdmin(UserAdmin):
    inlines = [PerfilInline]


admin.site.unregister(User)
admin.site.register(User, UsuarioConPerfilAdmin)
