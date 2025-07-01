from django.shortcuts import render, get_object_or_404
from .models import Anuncio, Empleado
from django.core.paginator import Paginator


def inicio(request):
    ultimos_anuncios = Anuncio.objects.filter(
        activo=True).order_by('-publicado')[:3]
    return render(request, 'index.html', {'ultimos_anuncios': ultimos_anuncios})


def anuncios(request):
    anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'web/anuncios.html', {'anuncios': anuncios})


def anuncio_detalle(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug, activo=True)
    return render(request, 'anuncio_detalle.html', {'anuncio': anuncio})


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


### PARA REDIRECCIONAR LAS SECCION#####
def blog_home(request):
    return render(request, 'blog-home.html')


def blog_post(request):
    return render(request, 'blog-post.html')
