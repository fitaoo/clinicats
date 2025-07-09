from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/', views.blog_home, name='blog_home'),
    path('contacto/', views.contacto_view, name='contact'),
    path('anuncio/<slug:slug>/', views.anuncio_detalle, name='anuncio_detalle'),
]
