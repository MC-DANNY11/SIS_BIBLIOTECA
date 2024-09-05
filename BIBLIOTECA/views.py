from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Inicio(request):
    return render(request, 'libros/libros.html')
