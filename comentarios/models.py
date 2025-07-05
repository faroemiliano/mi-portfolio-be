from django.db import models

# Create your models here.
class Comentario(models.Model):
    autor = models.CharField(max_length=100, default="Anonimo")
    email = models.EmailField(blank=True, null=True)     # puede quedar vacío
    mensaje = models.TextField(blank=True, null=True) 
    creado_en = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.autor} - {self.mensaje[:30]}..."