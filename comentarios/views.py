from rest_framework import generics
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from comentarios.utils.mensage_telegram import send_telegram_message

TELEGRAM_TOKEN = "8049716688:AAFT4-FYeNbyugHNyox7YzLdmqrk6dtsL_o"
TELEGRAM_CHAT_ID = "7813490283"

class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        comentario = serializer.save()

        mensaje = (
            f"📩 *Nuevo comentario recibido*\n"
            f"👤 Autor: {comentario.autor}\n"
            f"✉️ Email: {comentario.email}\n"
            f"💬 Mensaje: {comentario.mensaje}\n"
            f"🕒 Fecha: {comentario.creado_en}"
        )
        print("ENVIANDO MENSAJE A TELEGRAM...")
        send_telegram_message(
            TELEGRAM_TOKEN,
            TELEGRAM_CHAT_ID,
            mensaje
        )
