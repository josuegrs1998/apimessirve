# Generated by Django 3.1.1 on 2020-11-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201121_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Cuenta con esta direccion de E-Mail ya existe!'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
