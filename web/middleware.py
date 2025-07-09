from django.http import HttpResponseForbidden

# Lista de IPs autorizadas
IP_AUTORIZADAS = ["127.0.0.1", "192.168.0.1", "192.168.1.151"]


class BloquearAdminPorIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Detecta IP real incluso detrás de proxy
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")

        print("IP real detectada →", ip)

        if request.path.startswith("/admin/") and ip not in IP_AUTORIZADAS:
            return HttpResponseForbidden("🔒 Acceso al panel restringido por IP.")

        return self.get_response(request)
