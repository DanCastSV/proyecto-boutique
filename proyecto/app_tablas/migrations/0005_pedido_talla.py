# Generated by Django 4.1.3 on 2022-12-01 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tablas', '0004_tallas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='talla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_tablas.tallas'),
        ),
    ]
