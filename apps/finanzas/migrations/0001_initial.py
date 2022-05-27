# Generated by Django 4.0.4 on 2022-05-27 01:32

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=b'I01\n', max_length=100, null=True)),
                ('tipo_de_categoria', models.CharField(choices=[('F', 'Gasto Fijo(Obligatorio)'), ('N', 'Gasto Necesario(Sobrevivencia)'), ('P', 'Gasto Prescindible(Lujo)'), ('I', 'Ingreso de dinero'), ('C', 'Categoria Padre (admin)')], default='F', max_length=1)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='subcategoria', to='finanzas.categorias')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo_de_cuenta', models.CharField(choices=[('GRAL', 'General'), ('EFEC', 'Efectivo'), ('BANC', 'Cuenta Bancaria'), ('CRED', 'Tarjeta de Credito'), ('AHOR', 'Cuenta de ahorros'), ('EXTR', 'Extra'), ('SEGU', 'Seguro'), ('INVE', 'Inversión'), ('PRES', 'Prestamo'), ('HIPO', 'Hipoteca')], default='GRAL', max_length=4)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=350)),
            ],
            options={
                'verbose_name_plural': 'Forma de pagos',
            },
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_registro', models.CharField(choices=[('GAST', 'Gasto'), ('INGR', 'Ingreso'), ('TRAN', 'Transferencia')], default='GAST', max_length=4)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('nota', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_de_pago', models.DateField(default=datetime.date.today)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.categorias')),
                ('cuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.cuenta')),
                ('forma_de_pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finanzas.forma_de_pago')),
            ],
            options={
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
