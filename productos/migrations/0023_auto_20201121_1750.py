# Generated by Django 3.1.1 on 2020-11-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0022_auto_20201121_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('En Proceso', 'EN PROCESO'), ('Carrito', 'CARRITO'), ('Orden Cerrada', 'ORDEN CERRADA'), ('Orden Abierta', 'ORDEN ABIERTA')], default='Carrito', max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='empresaproducto',
            unique_together={('idEmpresa', 'idProducto')},
        ),
    ]