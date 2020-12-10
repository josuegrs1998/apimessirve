from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from productos.models import Producto


class ProductoSitemap(Sitemap):
    def items(self):
        return Producto.objects.all()
    
