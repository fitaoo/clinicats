from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ← usa el admin clásico (jazzmin lo personaliza automáticamente)
    path('admin/', admin.site.urls),
    path('', include('web.urls')),    # ← tus rutas principales
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
