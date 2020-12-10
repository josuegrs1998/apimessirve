# Generated by Django 3.1.1 on 2020-12-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0045_auto_20201207_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Orden Abierta', 'ORDEN ABIERTA'), ('Carrito', 'CARRITO'), ('Orden Cerrada', 'ORDEN CERRADA'), ('En Proceso', 'EN PROCESO')], default='Carrito', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto_orden',
            name='estado',
            field=models.CharField(choices=[('Orden Abierta', 'ORDEN ABIERTA'), ('Carrito', 'CARRITO'), ('Orden Cerrada', 'ORDEN CERRADA'), ('En Proceso', 'EN PROCESO')], default='Carrito', max_length=25),
        ),
    ]
