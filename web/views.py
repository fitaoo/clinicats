from django.shortcuts import render
from .models import Anuncio

def inicio(request):
    return render(request, 'index.html')

def anuncios(request):
    anuncios = Anuncio.objects.filter(activo=True).order_by('-publicado')
    return render(request, 'web/anuncios.html', {'anuncios': anuncios})

def blog_home(request):
    return render(request, 'blog-home.html')

def blog_post(request):
    return render(request, 'blog-post.html')

def contact(request):
    return render(request, 'contact.html')