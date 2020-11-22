from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import (Categoria, Cupon, EmpresaProducto, Empresa, Orden  ,
Subcategoria, Marca, Producto, TagProducto, Tags, Imagenes, TallaProducto, Talla, Producto_Orden, Login, Cliente)
from .serializers import (CategoriaSerializer, SubcategoriaSerializer, MarcaSerializer, SubcategoriaProductoSerializer,
ProductoSerializer, TallaSerializer, TallaProductoSerializer, TagProductoSerializer, TagSerializer,EmpresaSerializer 
, ImagenesSerializer, EmpresaProductoSerializer, CuponSerializer, OrdenSerializer, Producto_OrdenSerializer, LoginSerializer, ClienteSerializer)
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ListaCategoria(ListCreateAPIView):
    serializer_class = CategoriaSerializer
    #permission_classes =(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()
        
    def get_queryset(self):
        return Categoria.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre')


class DetalleCategoria(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = CategoriaSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
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

    def get_queryset(self):
        request = self.request.GET
        queryset = Producto.objects.all()
        if(request.get('subcategorias')):
            queryset = queryset.filter(subcategorias__nombre=request.get('subcategorias'))
        if(request.get('marca')):
            queryset = queryset.filter(marca__nombre=request.get('marca'))
        return queryset
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombre','codigoProducto')
    search_fields = ('nombre', 'descripcion')


class DetalleProducto(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = ProductoSerializer
   # permission_classes =(permissions.IsAuthenticated,)
    lookup_field='id'

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
class ListaEmpresaProducto(ListCreateAPIView):
    serializer_class = EmpresaProductoSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return EmpresaProducto.objects.all()
    
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
        return Orden.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'estado', 'no_Orden', 'idCliente')

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
    filter_fields = ('id', 'idOrden', 'idProducto')

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
        return Cliente.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'nombres', 'apellidos', 'email', 'activo')

class DetalleCliente(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = ClienteSerializer
    lookup_field='id'

    def get_queryset(self):
        return Cliente.objects.all()