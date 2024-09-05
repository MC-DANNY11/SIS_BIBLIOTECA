from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=15, choices=[('bibliotecario', 'Bibliotecario'), ('administrador', 'Administrador')], default='usuario')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email
class Socio(models.Model):
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=80)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido} - DNI: {self.dni}"
class Editorial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    año_publicacion = models.IntegerField(blank=True, null=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    cantidad_total = models.IntegerField(default=0)
    cantidad_disponible = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
class Prestamo(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=[('prestado', 'Prestado'), ('devuelto', 'Devuelto')], default='prestado')

    def __str__(self):
        return f"Prestamo de {self.socio} - Estado: {self.estado}"
class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"Detalle del Prestamo {self.prestamo.id} - Libro: {self.libro.titulo}"
class Inventario(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario del libro {self.libro.titulo} - Cantidad disponible: {self.cantidad_disponible}"
class MovimientoInventario(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=7, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Movimiento {self.tipo_movimiento} de {self.libro.titulo} - Cantidad: {self.cantidad}"
class HistorialCambio(models.Model):
    TABLAS_CHOICES = [
        ('Usuarios', 'Usuarios'),
        ('Socios', 'Socios'),
        ('Editoriales', 'Editoriales'),
        ('Libros', 'Libros'),
        ('Prestamos', 'Prestamos'),
        ('Detalle_Prestamos', 'Detalle_Prestamos'),
        ('Inventarios', 'Inventarios'),
        ('Movimientos_Inventario', 'Movimientos_Inventario'),
    ]
    TIPO_CAMBIO_CHOICES = [
        ('insertar', 'Insertar'),
        ('actualizar', 'Actualizar'),
        ('eliminar', 'Eliminar'),
    ]

    tabla_afectada = models.CharField(max_length=30, choices=TABLAS_CHOICES)
    id_registro_afectado = models.IntegerField()
    tipo_cambio = models.CharField(max_length=10, choices=TIPO_CAMBIO_CHOICES)
    usuario_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cambio en {self.tabla_afectada} - ID: {self.id_registro_afectado} - Tipo: {self.tipo_cambio}"
