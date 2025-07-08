"""from django.http import HttpResponseForbidden

# IPs permitidas individualmente
ALLOWED_ADMIN_IPS = [
    '192.168.1.106',  # Tu IP
    '127.0.0.1',      # Localhost IPv4
    '::1'             # Localhost IPv6
]

# Prefijos de IP permitidos (para permitir rangos como 192.168.1.*)
ALLOWED_PREFIXES = ['192.168.1.']

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            print(f"IP detectada: {ip}")  # 👈 Para depurar

            if ip in ALLOWED_ADMIN_IPS:
                return self.get_response(request)

            if any(ip.startswith(prefix) for prefix in ALLOWED_PREFIXES):
                return self.get_response(request)

            return HttpResponseForbidden("Acceso denegado al panel de administración.")
        return self.get_response(request)"""
