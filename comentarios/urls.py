from django.urls import path
from .views import ComentarioListCreateView

urlpatterns = [
    path('comentarios/', ComentarioListCreateView.as_view(), name='comentarios'),
]