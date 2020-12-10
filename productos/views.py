from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import (Categoria, Cupon, EmpresaProducto, Empresa, Orden  ,
Subcategoria, Marca, Producto, TagProducto, Tags, Imagenes, TallaProducto, Talla, Producto_Orden, Login, Cliente)
from .serializers import (CategoriaSerializer, SubcategoriaSerializer, MarcaSerializer, SubcategoriaProductoSerializer,
ProductoSerializer, TallaSerializer, TallaProductoSerializer, TagProductoSerializer, TagSerializer,EmpresaSerializer 
, ImagenesSerializer, EmpresaProductoSerializer, CuponSerializer, OrdenSerializer, Producto_OrdenSerializer, LoginSerializer, ClienteSerializer, SimpleProductoSerializer)
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.db import connection
# Create your views here.

class ListaCategoria(ListCreateAPIView):
    serializer_class = CategoriaSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()
        
    def get_queryset(self):
        queryset = Categoria.objects.all()
        print(queryset.query)
        return Categoria.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre')


class DetalleCategoria(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = CategoriaSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        queryset = Categoria.objects.all()
        print(queryset.query)
        return Categoria.objects.all()

 #------------------------------------------------------------------------------------------------------#
class ListaSubcategoria(ListCreateAPIView):
    serializer_class = SubcategoriaSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        
        return Subcategoria.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre', 'idCategoria')


class DetalleSubcategoria(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = SubcategoriaSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Subcategoria.objects.all()

#------------------------------------------MARCA---------------------------------------------#

class ListaMarca(ListCreateAPIView):
    serializer_class = MarcaSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Marca.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre')


class DetalleMarca(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = MarcaSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Marca.objects.all()

#------------------------------------------PRODUCTO---------------------------------------------#

class ListaProducto(ListCreateAPIView):
    serializer_class = ProductoSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()
    def post(self, request, *args, **kwargs):
        serializer = SimpleProductoSerializer(data=request.data)
        if serializer.is_valid():
            producto = serializer.save()
            serializer = SimpleProductoSerializer(producto)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        request = self.request.GET
        queryset = Producto.objects.all()
        if(request.get('subcategoria')):
            queryset = queryset.filter(subcategorias__nombre=request.get('subcategoria'))
        if(request.get('marca')):
            queryset = queryset.filter(marca__nombre=request.get('marca'))
        if(request.get('tags')):
            queryset = queryset.filter(tags__nombre = request.get('tags'))
        if(request.get('exclude_empresa')):
            queryset = queryset.exclude(empresaproducto__idEmpresa_id=request.get('exclude_empresa'))

        print(queryset.query)
        return queryset
    
    filter_backends = (DjangoFilterBackend, SearchFilter)   
    filter_fields = ('id', 'nombre','codigoProducto')
    search_fields = ('nombre', 'descripcion')


class DetalleProducto(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = ProductoSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def patch(self, request, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=kwargs['producto_id'])
        serializer = SimpleProductoSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            producto = serializer.save()
            return Response(SimpleProductoSerializer(producto).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Producto.objects.all()

#------------------------------------------SUBCATEGORIA PRODUCTO---------------------------------------------#

class ListaSubProducto(ListCreateAPIView):
    serializer_class = SubcategoriaProductoSerializer
    #permission_classes =(permissions.IsAuthenticated,)

    def get_queryset(self):
        return Subcategoria.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = '__all__'

    search_fields = ('producto_set')


#class DetalleSubProducto(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
 #   serializer_class = SubcategoriaProductoSerializer
   # permission_classes =(permissions.IsAuthenticated,)
#    lookup_field='id'

 #   def get_queryset(self):
  #      return SubcategoriaProducto.objects.all()



#------------------------------------------TAG---------------------------------------------#

class ListaTag(ListCreateAPIView):
    serializer_class = TagSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Tags.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre')


class DetalleTag(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = TagSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Tags.objects.all()

#------------------------------------------TagProductos---------------------------------------------#

class ListaTagProductos(ListCreateAPIView):
    serializer_class = TagProductoSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return TagProducto.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'idProducto', 'idTag')


class DetalleTagProductos(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = TagProductoSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return TagProducto.objects.all()


#------------------------------------------Imagen---------------------------------------------#

class ListaImagenes(ListCreateAPIView):
    serializer_class = ImagenesSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Imagenes.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'idProducto', 'imagen')


class DetalleImagenes(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = ImagenesSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Imagenes.objects.all()


#------------------------------------------Talla---------------------------------------------#

class ListaTalla(ListCreateAPIView):
    serializer_class = TallaSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Talla.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'tamanio')


class DetalleTalla(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = TallaSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Talla.objects.all()

#------------------------------------------TallaProducto---------------------------------------------#

class ListaTallaProducto(ListCreateAPIView):
    serializer_class = TallaProductoSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return TallaProducto.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'idtalla', 'idProducto')


class DetalleTallaProducto(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = TallaProductoSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return TallaProducto.objects.all()

#------------------------------------------Empresa---------------------------------------------#
class ListaEmpresa(ListCreateAPIView):
    serializer_class = EmpresaSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Empresa.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre', 'ruc')

class DetalleEmpresa(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = EmpresaSerializer
    lookup_field='id'

    def get_queryset(self):
        return Empresa.objects.all()

#------------------------------------------EmpresaProducto---------------------------------------------#


class GameFilter(filters.FilterSet):
    precioBase = filters.RangeFilter(name = 'precioBase')

    class Meta:
        model = EmpresaProducto
        fields = ['precioBase']

class ListaEmpresaProducto(ListCreateAPIView):
    serializer_class = EmpresaProductoSerializer
    def perform_create(self, serializer):
        serializer.save()
    
 
    def get_queryset(self):
        request = self.request.GET
       
        queryset = EmpresaProducto.objects.all()
        if(request.get('minimo')): # Ejemplo: http://127.0.0.1:8000/api/empresaproducto?minimo=10&maximo=30
          minimo = request.get('minimo') 
          maximo = request.get('maximo')
          queryset = EmpresaProducto.objects.filter(precioBase__range = (minimo, maximo))
          print(queryset.query)
        return queryset
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'idEmpresa', 'idProducto')

class DetalleEmpresaProducto(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = EmpresaProductoSerializer
    lookup_field='id'

    def get_queryset(self):
        return EmpresaProducto.objects.all()


#------------------------------------------Cupon---------------------------------------------#
class ListaCupon(ListCreateAPIView):
    serializer_class = CuponSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Cupon.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'codigo')

class DetalleCupon(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = CuponSerializer
    lookup_field='id'

    def get_queryset(self):
        return Cupon.objects.all()


#------------------------------------------Orden---------------------------------------------#
class ListaOrden(ListCreateAPIView):
    serializer_class = OrdenSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        request = self.request.GET
        queryset = Orden.objects.all()
        if(request.get('exclude_estado')):
            queryset = queryset.exclude(estado=request.get('exclude_estado'))
        return queryset
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'estado', 'no_Orden', 'idUsuario')

class DetalleOrden(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = OrdenSerializer
    lookup_field='id'

    def get_queryset(self):
        return Orden.objects.all()

#------------------------------------------Producto_Orden---------------------------------------------#
class ListaProducto_Orden(ListCreateAPIView):
    serializer_class = Producto_OrdenSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Producto_Orden.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'idOrden', 'idProducto', 'idEmpresa')

class DetalleProducto_Orden(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = Producto_OrdenSerializer
    lookup_field='id'

    def get_queryset(self):
        return Producto_Orden.objects.all()

#------------------------------------------LOGIN---------------------------------------------#
class ListaLogin(ListCreateAPIView):
    serializer_class = LoginSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Login.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'email')

class DetalleLogin(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = LoginSerializer
    lookup_field='id'

    def get_queryset(self):
        return Login.objects.all()

#------------------------------------------Cliente---------------------------------------------#
class ListaCliente(ListCreateAPIView):
    serializer_class = ClienteSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        print(connection.queries)
        return Cliente.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombres', 'apellidos', 'email', 'activo')

class DetalleCliente(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = ClienteSerializer
    lookup_field='id'

    def get_queryset(self):
        return Cliente.objects.all()


