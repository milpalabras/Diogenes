# Generated by Django 4.0.4 on 2022-05-19 22:26

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_alter_registros_options_alter_registros_importe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#FF0000', image_field=None, max_length=18, null=True, samples=None),
        ),
    ]
