# Generated by Django 3.1.1 on 2020-11-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0023_auto_20201121_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Carrito', 'CARRITO'), ('Orden Abierta', 'ORDEN ABIERTA'), ('Orden Cerrada', 'ORDEN CERRADA'), ('En Proceso', 'EN PROCESO')], default='Carrito', max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='tallaproducto',
            unique_together={('idEmpresa', 'idProducto', 'idtalla')},
        ),
    ]
