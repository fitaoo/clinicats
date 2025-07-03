from django.shortcuts import render, get_object_or_404
from .models import Anuncio, Empleado
from django.core.paginator import Paginator

# Propósito: Renderiza la página principal de la web


def inicio(request):
    ultimos_anuncios = Anuncio.objects.filter(
        activo=True).order_by('-publicado')[:3]
    return render(request, 'index.html', {'ultimos_anuncios': ultimos_anuncios})


# Propósito: Muestra un listado completo de todos los anuncios activos.
def anuncios(request):
    anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'web/anuncios.html', {'anuncios': anuncios})


# Propósito: Muestra el directorio telefónico.
def contact(request):
    print("🔍 Esta es la función correcta")

    direccion = request.GET.get('direccion')
    empleados = Empleado.objects.filter(
        direccion=direccion) if direccion else Empleado.objects.all()

    paginator = Paginator(empleados, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contact.html', {
        'page_obj': page_obj,
        'direccion': direccion,
    })

# Propósito: Muestra la vista principal de “Blog home” con anuncio mas reciente.


def blog_home(request):
    anuncio_principal = Anuncio.objects.filter(
        activo=True).order_by('-publicado').first()
    otros_anuncios = Anuncio.objects.filter(
        activo=True).order_by('-publicado')[1:4]

    return render(request, 'blog-home.html', {
        'anuncio': anuncio_principal,
        'otros_anuncios': otros_anuncios
    })

# Muestra una noticia individual en su propia página usando la plantilla principal blog-post.html


def anuncio_detalle(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug, activo=True)
    return render(request, 'blog-post.html', {'anuncio': anuncio})
