from django.http import HttpResponseForbidden

# IPs que pueden acceder al sitio web
ALLOWED_SITE_IPS = ['192.168.1.108', '192.168.0.12', '192.168.1.151']

# IPs que pueden acceder al panel admin
ALLOWED_ADMIN_IPS = ['192.168.1.108', '192.168.0.12', '192.168.1.151']


class DualIPRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')

        # Bloqueo total si la IP no está permitida para el sitio
        if client_ip not in ALLOWED_SITE_IPS:
            return HttpResponseForbidden("Acceso denegado: IP no autorizada para el sitio")

        # Bloqueo adicional si intenta entrar al admin y no tiene permiso
        if request.path.startswith('/admin') and client_ip not in ALLOWED_ADMIN_IPS:
            return HttpResponseForbidden("Acceso denegado: IP no autorizada para el panel admin")

        return self.get_response(request)
