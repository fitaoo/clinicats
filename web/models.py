from django.db import models
from django.utils.text import slugify
import os
from django.core.files import File
from django.contrib.auth.models import User

# ESTO ES PARA SECCION AGREGAR ANUNCIOS EN ADMIN
from django.db import models
from django.utils.text import slugify


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


class Empleado(models.Model):
    DIRECCIONES = [
        ('ADMISION_ELECTIVA', 'Admisión electiva'),
        ('ADMISION_EMERGENCIA', 'Admisión emergencia'),
        ('ADMINISTRACION', 'Administración'),
        ('ARQUITECTURA', 'Arquitectura'),
        ('AUX_FARMACIA', 'Aux farmacia'),
        ('CAMARERAS', 'Camareras'),
        ('COBRANZA', 'Cobranza'),
        ('COMPRAS', 'Compras'),
        ('COMPRAS_FARMACIA', 'Compras farmacia'),
        ('CONTABILIDAD', 'Contabilidad'),
        ('COCINA', 'Cocina'),
        ('EMERGENCIA', 'Emergencia'),
        ('ESTERILIZACION', 'Esterilización'),
        ('ESTAR_ENFERMERIA', 'Estar enfermería'),
        ('ESTAR_ENFERMERIA_2', 'Estar enfermería 2'),
        ('FARMACIA', 'Farmacia'),
        ('FACTURACION', 'Facturación'),
        ('HISTORIAS_MEDICAS', 'Historias médicas'),
        ('MARKETING', 'Marketing'),
        ('PRESUPUESTO', 'Presupuesto'),
        ('PRESIDENCIA', 'Presidencia'),
        ('PROTOCOLO', 'Protocolo'),
        ('QUIROFANO', 'Quirofano'),
        ('REGENTE', 'Regente'),
        ('RECURSOS_HUMANOS', 'Recursos humanos'),
        ('SERVICIOS_GENERALES', 'Servicios generales'),
        ('TECNOLOGIA', 'Tecnología'),
        ('UCI', 'UCI'),
        ('UTIN', 'UTIN'),
        ('AUDITORA', 'Auditora'),
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)
    direccion = models.CharField(max_length=30, choices=DIRECCIONES)

    def save(self, *args, **kwargs):
        if not self.foto:
            # asegúrate de que el archivo exista
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
