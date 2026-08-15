import logging

logger = logging.getLogger('django')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Captura información básica de la petición entrante
        method = request.method
        path = request.path
        ip = request.META.get('REMOTE_ADDR', 'Unknown')
        
        # Imprime directamente en la salida estándar (capturada por Render)
        print(f"[HTTP Request] IP: {ip} | Method: {method} | Path: {path}")

        response = self.get_response(request)
        return response