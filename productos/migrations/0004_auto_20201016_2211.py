# Generated by Django 3.1.1 on 2020-10-17 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_subcategoria_productos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='subategorias',
            new_name='subcategorias',
        ),
    ]
