from rest_framework import generics
from .models import Comentario
from .serializers import ComentarioSerializer
from django.core.mail import send_mail
from django.conf import settings

class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all().order_by('creado_en')
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        comentario = serializer.save()

        # Enviar email al administrador (vos)
        send_mail(
            subject=f"Nuevo comentario de {comentario.autor}",
            message=f"""
            Has recibido un nuevo comentario.

            Nombre: {comentario.autor}
            Email: {comentario.email}
            Mensaje: {comentario.mensaje}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['faroemiliano@gmail.com'],  # <-- reemplazalo con tu email
            fail_silently=False,
        )