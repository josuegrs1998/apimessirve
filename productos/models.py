from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    codigoProducto = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=120)
    activo = models.BooleanField()
    tipoMaterial = models.CharField(max_length=30)
    exento = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    subcategorias = models.ManyToManyField(Subcategoria)

    def __str__(self):
        return self.nombre


class Tags(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre
    
class TagProducto(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idTag = models.ForeignKey(Tags, on_delete=models.CASCADE)

class Imagenes(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'images')

class Talla(models.Model):
    tamanio = models.CharField(max_length=15)
    def __str__(self):
        return self.tamanio

class TallaProducto(models.Model):
    idtalla = models.ForeignKey(Talla, on_delete=models.CASCADE )
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=30)
    ruc = models.CharField(max_length=10)

class EmpresaProducto(models.Model):
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=16, decimal_places=2)
    precioBase = models.DecimalField(max_digits=16, decimal_places=2)

class Cupon(models.Model):
    activo = models.BooleanField()
    cantidad = models.DecimalField(max_digits=16, decimal_places=2)
    minimoAplicable = models.DecimalField(max_digits=16, decimal_places=2)
    codigo = models.CharField(max_length=50)


ORDER_CHOICES ={
    ('Carrito','CARRITO'),
    ('Orden Abierta', 'ORDEN ABIERTA'),
    ('Orden Cerrada','ORDEN CERRADA')
}
class Orden(models.Model):
    estado = models.CharField(max_length=25, choices=ORDER_CHOICES, default='Carrito')
    no_Orden = models.CharField(max_length = 10)
    impuesto = models.DecimalField(max_digits=16, decimal_places=2)
    envio = models.DecimalField(max_digits=16, decimal_places=2)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    fecha_ingreso = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    idcupon = models.ForeignKey(Cupon, null=True,on_delete = models.CASCADE)

class Producto_Orden(models.Model):
    idOrden = models.ForeignKey(Producto, on_delete= models.CASCADE)
    idProducto = models.ForeignKey(Orden, on_delete = models.CASCADE)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    cantidad = models.IntegerField()
    iva = models.DecimalField(max_digits=16, decimal_places=2)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)


    







