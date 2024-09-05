from django.contrib import admin
from .models import Usuario, Socio, Libro,Editorial,Prestamo, DetallePrestamo,Inventario,MovimientoInventario,HistorialCambio

admin.site.register(Usuario)
admin.site.register(Socio)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
admin.site.register(MovimientoInventario)
admin.site.register(Inventario)
admin.site.register(HistorialCambio)

