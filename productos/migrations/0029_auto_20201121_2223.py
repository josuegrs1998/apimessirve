# Generated by Django 3.1.1 on 2020-11-22 04:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0028_auto_20201121_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Carrito', 'CARRITO'), ('Orden Cerrada', 'ORDEN CERRADA'), ('En Proceso', 'EN PROCESO'), ('Orden Abierta', 'ORDEN ABIERTA')], default='Carrito', max_length=25),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_entrega',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='orden',
            name='no_Orden',
            field=models.UUIDField(),
        ),
    ]