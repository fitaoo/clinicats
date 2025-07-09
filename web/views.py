from django.shortcuts import render, get_object_or_404
from .models import Anuncio, Empleado, Departamento
from django.core.paginator import Paginator

# Propósito: Renderiza la página principal de la web


def inicio(request):
    ultimos_anuncios = Anuncio.objects.filter(
        activo=True).order_by('-publicado')[:3]
    return render(request, 'index.html', {'ultimos_anuncios': ultimos_anuncios})


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


def blog_home(request):
    anuncios_qs = Anuncio.objects.filter(activo=True).order_by('-publicado')
    anuncio_principal = anuncios_qs.first()

    # Excluir el principal de la lista paginada
    paginator = Paginator(anuncios_qs[1:], 3)  # 3 noticias por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog-home.html', {
        'anuncio': anuncio_principal,
        'otros_anuncios': page_obj  # ahora es el paginado
    })


def blog_home(request):
    anuncios_qs = Anuncio.objects.filter(activo=True).order_by('-publicado')
    anuncio_principal = anuncios_qs.first()

    # excluye el primero, pagina el resto
    paginator = Paginator(anuncios_qs[1:], 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog-home.html', {
        'anuncio': anuncio_principal,
        'otros_anuncios': page_obj
    })


# Muestra una noticia individual en su propia página usando la plantilla principal blog-post.html


def anuncio_detalle(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug, activo=True)
    return render(request, 'blog-post.html', {'anuncio': anuncio})

# Para filtrar deparamentos y crear botones


def contacto_view(request):
    direccion = request.GET.get("direccion")
    departamentos = Departamento.objects.all().order_by("nombre")

    if direccion:
        empleados = Empleado.objects.filter(
            departamento__nombre__iexact=direccion)
    else:
        empleados = Empleado.objects.all()

    paginator = Paginator(empleados, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "direccion": direccion,
        "departamentos": departamentos,
        "page_obj": page_obj,
    }
    return render(request, "contact.html", context)
