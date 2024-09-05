from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def Index(request):
    return render(request, 'libros/index.html')
def Libro(request):
    return render(request, 'libros/libros.html')
def Editorial(request):
    return render(request, 'libros/editorial.html')
def Socio(request):
    return render(request, 'libros/socios.html')
def Usuario(request):
    return render(request, 'libros/usuarios.html')
def Prestamo(request):
    return render(request, 'libros/prestamos.html')
def Inventario(request):
    return render(request, 'libros/inventario.html')
def Historial(request):
    return render(request, 'libros/historial.html')
