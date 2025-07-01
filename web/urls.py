from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/', views.blog_home, name='blog_home'),
    path('blog/post/', views.blog_post, name='blog_post'),
    path('contacto/', views.contact, name='contact'),
    path('anuncio/<slug:slug>/', views.anuncio_detalle, name='anuncio_detalle'),
]
