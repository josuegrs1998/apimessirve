# Generated by Django 3.1.1 on 2020-12-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0050_auto_20201209_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Orden Cerrada', 'ORDEN CERRADA'), ('Carrito', 'CARRITO'), ('Orden Abierta', 'ORDEN ABIERTA'), ('En Proceso', 'EN PROCESO')], default='Carrito', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tags',
            field=models.ManyToManyField(null=True, to='productos.Tags'),
        ),
        migrations.AlterField(
            model_name='producto_orden',
            name='estado',
            field=models.CharField(choices=[('Orden Cerrada', 'ORDEN CERRADA'), ('Carrito', 'CARRITO'), ('Orden Abierta', 'ORDEN ABIERTA'), ('En Proceso', 'EN PROCESO')], default='Carrito', max_length=25),
        ),
    ]
