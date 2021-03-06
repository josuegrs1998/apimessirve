# Generated by Django 3.1.1 on 2020-11-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_producto_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='imagen',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Orden Cerrada', 'ORDEN CERRADA'), ('Carrito', 'CARRITO'), ('Orden Abierta', 'ORDEN ABIERTA')], default='Carrito', max_length=25),
        ),
    ]
