from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ManagerMensaje(models.Manager):

    def inbox_user(self, user):       
        
        return self.filter(
            destinatario=user,
            destinatario_borrado_el__isnull=True,
        )

    def salida_user(self, user):
        
        return self.filter(
            remitente=user,
            remitente_borrado_el__isnull=True,
        )

    def papelera_user(self, user):
        
        return self.filter(
            destinatario=user,
            destinatario_borrado_el__isnull=False,
        ) | self.filter(
            remitente=user,
            remitente_borrado_el__isnull=False,
        )



class Mensaje(models.Model):
    
    asunto = models.CharField(_("Subject"), max_length=140)
    cuerpo = models.TextField(_("Body"))
    remitente = models.ForeignKey(User, related_name='sent_messages', verbose_name=_("Sender"), on_delete=models.PROTECT)
    destinatario = models.ForeignKey(User, related_name='received_messages', null=True, blank=True, verbose_name=_("Recipient"), on_delete=models.SET_NULL)
    parent_msg = models.ForeignKey('self', related_name='next_messages', null=True, blank=True, verbose_name=_("Parent message"), on_delete=models.SET_NULL)
    enviado_el = models.DateTimeField(_("sent at"), null=True, blank=True)
    leido_el = models.DateTimeField(_("read at"), null=True, blank=True)
    respondido_el = models.DateTimeField(_("replied at"), null=True, blank=True)
    remitente_borrado_el = models.DateTimeField(_("Sender deleted at"), null=True, blank=True)
    destinatario_borrado_el = models.DateTimeField(_("Recipient deleted at"), null=True, blank=True)

    objects = ManagerMensaje()

    def nuevo(self):        
        if self.leido_el is not None:
            return False
        return True

    def respondido(self):
        
        if self.respondido_el is not None:
            return True
        return False

    def __str__(self):
        return self.asunto

    def get_absolute_url(self):
        return reverse('messages_detail', args=[self.id])

    def save(self, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        super(Mensaje, self).save(**kwargs)

    class Meta:
        ordering = ['-enviado_el']
        verbose_name = _("Mensaje")
        verbose_name_plural = _("Mensajes")


def inbox_count(user):
    """
    returns the number of unread messages for the given user but does not
    mark them seen
    """
    return Mensaje.objects.filter(destinatario=user, leido_el__isnull=True, destinatario_borrado_el__isnull=True).count()

def mensajes_sin_leer(user):

    return Mensaje.objects.filter(destinatario=user, leido_el__isnull=True, destinatario_borrado_el__isnull=True)



