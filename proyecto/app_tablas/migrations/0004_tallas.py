# Generated by Django 4.1.3 on 2022-12-01 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tablas', '0003_rename_nombre_pedido_nombre_p_pedido_nombre_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tallas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(max_length=1)),
            ],
        ),
    ]
