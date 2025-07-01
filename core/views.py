from web.models import Ultimo, Historia, Anuncio
from django.shortcuts import render, get_object_or_404

def inicio(request):
    ultimos_anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')[:3]
    return render(request, 'index.html', {'ultimos_anuncios': ultimos_anuncios})

def blog_home(request):
    historial = Anuncio.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'blog-home.html', {'anuncios': historial})

def anuncio_detalle(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug, activo=True)
    return render(request, 'anuncio_detalle.html', {'anuncio': anuncio})
