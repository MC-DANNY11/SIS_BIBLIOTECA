from django.contrib import admin
from django.urls import path
from . import views  # Asegúrate de que esto esté correcto

urlpatterns = [
    path('', views.Inicio, name='inicio'),
]
