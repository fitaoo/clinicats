from django.db import models
from django.utils.text import slugify
import os
from django.core.files import File
from django.contrib.auth.models import User

# ESTO ES PARA SECCION AGREGAR ANUNCIOS EN ADMIN


class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='anuncios/', blank=True, null=True)
    publicado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='anuncios')  # 🔗 Nuevo campo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        if not self.imagen:
            self.imagen.name = 'defaults/Anuncios.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
 # ESTO ES PARA SECCION AGREGA EN ADMIN PARA SUBIR EMPLEADOS


class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='empleados'
    )

    def save(self, *args, **kwargs):
        if not self.foto:
            default_path = os.path.join('media', 'empleados', 'default.png')
            if os.path.exists(default_path):
                with open(default_path, 'rb') as f:
                    self.foto.save('default.png', File(f), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        default='avatars/avatar.png'
    )

    def __str__(self):
        return self.user.username
