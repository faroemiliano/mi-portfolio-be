from rest_framework import generics
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from comentarios.utils.mensage_telegram import send_telegram_message
from threading import Thread
import os


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    raise RuntimeError("Telegram credentials no configuradas")

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
        Thread(
            target=send_telegram_message,
            args=(mensaje,),
            daemon=True
        ).start()
