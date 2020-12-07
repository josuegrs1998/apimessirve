from rest_framework.serializers import ModelSerializer
from .models import (Categoria,Subcategoria, Marca, Producto, Tags, TagProducto, 
Imagenes, Talla, TallaProducto, Empresa, EmpresaProducto, Cupon, Orden, Producto_Orden, Login, Cliente)

class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields =['id','nombre', 'descripcion']


class SubcategoriaSerializer(ModelSerializer):
    idCategoria = CategoriaSerializer()

    class Meta:
        model = Subcategoria
        fields = '__all__'

class MarcaSerializer(ModelSerializer):

    class Meta:
        model = Marca
        fields =['id','nombre', 'descripcion']

class ImagenesSerializer(ModelSerializer):

    class Meta: 
        model = Imagenes
        fields = ['id', 'idProducto', 'imagen']

class TallaSerializer(ModelSerializer):

    class Meta:
        model = Talla
        fields = ['id', 'tamanio']

class TallaProductoSerializer(ModelSerializer):
    idtalla = TallaSerializer()
    class Meta:
        model = TallaProducto
        fields = ['id', 'idtalla', 'idProducto', 'cantidad', 'idEmpresa']

class EmpresaSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'descripcion', 'telefono', 'correo', 'ruc']


class ProductoSerializerT(ModelSerializer):
    
    class Meta:
        model = Producto
        fields = '__all__'

class EmpresaProductoSerializer(ModelSerializer):
    idEmpresa = EmpresaSerializer()
    idProducto = ProductoSerializerT()
    class Meta:
        model = EmpresaProducto
        fields = ['id', 'idEmpresa', 'idProducto', 'cantidad', 'descuento', 'precioBase']


class OrdenSerializer(ModelSerializer):

    class Meta:
        model = Orden
        fields = ['id', 'estado', 'no_Orden', 'impuesto', 'envio', 'subtotal', 'total', 'fecha_ingreso', 'fecha_entrega', 'idcupon', 'idUsuario']

class Producto_OrdenSerializer(ModelSerializer):

    class Meta:
        model = Producto_Orden
        fields = ['id', 'idOrden', 'idProducto', 'precio', 'cantidad', 'iva', 'subtotal', 'total', 'idEmpresa']


class TagSerializer(ModelSerializer):
    
    class Meta:
        model = Tags
        fields =['id', 'nombre']

class TagProductoSerializer(ModelSerializer):
    idTag = TagSerializer()
    

    class Meta:
        model = TagProducto
        fields =['id', 'idTag', 'idProducto']

class ProductoSerializer(ModelSerializer):
    subcategorias = SubcategoriaSerializer(many=True)
    marca = MarcaSerializer()
    imagenes_set = ImagenesSerializer(many=True)
    tallaproducto_set = TallaProductoSerializer(many=True)
    empresaproducto_set = EmpresaProductoSerializer(many=True)
    producto_orden_set = Producto_OrdenSerializer(many=True)
    tagproducto_set = TagProductoSerializer(many=True)
    tags = TagSerializer (many = True)
    class Meta:
        model = Producto
        fields = '__all__'

class SubcategoriaProductoSerializer(ModelSerializer):
    producto_set = ProductoSerializer(many=True)
    class Meta:
        model = Subcategoria
        fields ='__all__'


class CuponSerializer(ModelSerializer):

    class Meta:
        model = Cupon
        fields = ['id', 'activo', 'cantidad', 'minimoAplicable', 'codigo']
    
class LoginSerializer(ModelSerializer):
    
    class Meta:
        model = Login
        fields = ['id', 'email', 'clave']

class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id', 'nombres', 'apellidos', 'telefono', 'email', 'activo', 'direccion', 'idLogin']