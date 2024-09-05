from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('libros', views.Libro, name='libros'),
    path('editorial', views.Editorial, name='editorial'),
    path('socios', views.Socio, name='socios'),
    path('usuarios', views.Usuario, name='usuarios'),
    path('prestamos', views.Prestamo, name='prestamos'),
    path('inventario', views.Inventario, name='inventario'),
    path('historial', views.Historial, name='historial'),
]
