from django.shortcuts import render, get_object_or_404
from .models import Anuncio

def inicio(request):
    ultimos_anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')[:3]
    return render(request, 'index.html', {'ultimos_anuncios': ultimos_anuncios})

def anuncios(request):
    anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'web/anuncios.html', {'anuncios': anuncios})

def blog_home(request):
    return render(request, 'blog-home.html')

def blog_post(request):
    return render(request, 'blog-post.html')

def contact(request):
    return render(request, 'contact.html')

def anuncio_detalle(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug, activo=True)
    return render(request, 'anuncio_detalle.html', {'anuncio': anuncio})

