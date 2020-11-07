# Generated by Django 3.1.1 on 2020-11-07 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=16)),
                ('cantidad', models.IntegerField()),
                ('iva', models.DecimalField(decimal_places=2, max_digits=16)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=16)),
                ('total', models.DecimalField(decimal_places=2, max_digits=16)),
                ('idOrden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.orden')),
            ],
        ),
    ]