# Generated by Django 4.1.3 on 2022-12-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tablas', '0005_pedido_talla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(null=True),
        ),
    ]