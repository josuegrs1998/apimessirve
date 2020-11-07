from django.contrib import admin
from .models import Categoria,Orden, Producto_Orden, Cupon,Subcategoria,EmpresaProducto, Marca, Producto, Tags, TagProducto, Imagenes, Talla, TallaProducto, Empresa


admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Marca)
admin.site.register(Producto)
#admin.site.register(SubcategoriaProducto)
admin.site.register(Tags)
admin.site.register(TagProducto)
admin.site.register(Imagenes)
admin.site.register(Talla)
admin.site.register(TallaProducto)
admin.site.register(Empresa)
admin.site.register(EmpresaProducto)
admin.site.register(Cupon)
admin.site.register(Orden)
admin.site.register(Producto_Orden)