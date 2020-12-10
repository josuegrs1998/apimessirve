from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from productos.models import Producto, Categoria



class ProductoSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Producto.objects.all()
    

    
class CategoriaSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'
    def items(self):
        return Categoria.objects.all()

