# Generated by Django 4.0.4 on 2022-06-02 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=140, verbose_name='Subject')),
                ('cuerpo', models.TextField(verbose_name='Body')),
                ('enviado_el', models.DateTimeField(blank=True, null=True, verbose_name='sent at')),
                ('leido_el', models.DateTimeField(blank=True, null=True, verbose_name='read at')),
                ('respondido_el', models.DateTimeField(blank=True, null=True, verbose_name='replied at')),
                ('remitente_borrado_el', models.DateTimeField(blank=True, null=True, verbose_name='Sender deleted at')),
                ('destinatario_borrado_el', models.DateTimeField(blank=True, null=True, verbose_name='Recipient deleted at')),
                ('destinatario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('parent_msg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_messages', to='mensajeria.mensaje', verbose_name='Parent message')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['-enviado_el'],
            },
        ),
    ]
