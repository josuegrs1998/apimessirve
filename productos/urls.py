from django.urls import path
from .views import (ListaCategoria, DetalleCategoria, ListaSubcategoria, ListaImagenes,
DetalleImagenes, ListaTalla, DetalleTalla, ListaTallaProducto, DetalleTallaProducto,
DetalleSubcategoria,ListaMarca, DetalleMarca, ListaProducto, ListaTag, DetalleTag,
ListaTagProductos, DetalleTagProductos, DetalleProducto, ListaSubProducto, ListaEmpresa, DetalleEmpresa, 
ListaEmpresaProducto, DetalleEmpresaProducto, ListaCupon, DetalleCupon, ListaOrden, DetalleOrden, ListaProducto_Orden
, DetalleProducto_Orden)


urlpatterns =[
    path('categorias', ListaCategoria.as_view()),
    path('categorias/<int:id>', DetalleCategoria.as_view()),
    path('subcategorias', ListaSubcategoria.as_view()),
    path('subcategorias/<int:id>', DetalleSubcategoria.as_view()),
    path('marcas', ListaMarca.as_view()),
    path('marcas/<int:id>', DetalleMarca.as_view()),
    path('productos', ListaProducto.as_view()),
    path('productos/<int:id>', DetalleProducto.as_view()),
    path('subproductos', ListaSubProducto.as_view()),
    #path('subproductos/<int:id>', DetalleSubProducto.as_view()),
    path('tags', ListaTag.as_view()),
    path('tags/<int:id>', DetalleTag.as_view()),
    path('tagproductos', ListaTagProductos.as_view()),
    path('tagproductos/<int:id>', DetalleTagProductos.as_view()),
    path('imagenes', ListaImagenes.as_view()),
    path('imagenes/<int:id>', DetalleImagenes.as_view()),
    path('talla', ListaTalla.as_view()),
    path('talla/<int:id>', DetalleTalla.as_view()),
    path('tallaproducto', ListaTallaProducto.as_view()),
    path('tallaproducto/<int:id>', DetalleTallaProducto.as_view()),
    path('empresa', ListaEmpresa.as_view()),
    path('empresa/<int:id>', DetalleEmpresa.as_view()),
    path('empresaproducto', ListaEmpresaProducto.as_view()),
    path('empresaproducto/<int:id>', DetalleEmpresaProducto.as_view()),
    path('cupon', ListaCupon.as_view()),
    path('cupon/<int:id>', DetalleCupon.as_view()),
    path('orden', ListaOrden.as_view()),
    path('orden/<int:id>', DetalleOrden.as_view()),
    path('productoorden', ListaProducto_Orden.as_view()),
    path('productoorden/<int:id>', DetalleProducto_Orden.as_view())

]