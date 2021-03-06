# Generated by Django 3.1.1 on 2020-11-22 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0026_auto_20201121_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='correo',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='login',
            name='username',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('Carrito', 'CARRITO'), ('En Proceso', 'EN PROCESO'), ('Orden Abierta', 'ORDEN ABIERTA'), ('Orden Cerrada', 'ORDEN CERRADA')], default='Carrito', max_length=25),
        ),
    ]
