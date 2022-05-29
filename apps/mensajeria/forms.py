from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from mensajeria.models import Mensaje
from mensajeria.fields import CommaSeparatedUserField

class ComposeForm(forms.Form):
    
    destinatario = CommaSeparatedUserField(label=_(u"Recipient"))
    asunto = forms.CharField(label=_(u"Subject"), max_length=140)
    cuerpo = forms.CharField(label=_(u"Body"), widget=SummernoteWidget())


    def __init__(self, *args, **kwargs):
        recipient_filter = kwargs.pop('recipient_filter', None)
        super(ComposeForm, self).__init__(*args, **kwargs)
        if recipient_filter is not None:
            self.fields['destinatario']._recipient_filter = recipient_filter


    def save(self, remitente, parent_msg=None):
        destinatario = self.cleaned_data['destinatario']
        asunto = self.cleaned_data['asunto']
        cuerpo = self.cleaned_data['cuerpo']
        mensaje_list = []
        for r in destinatario:
            msg = Mensaje(
                remitente = remitente,
                destinatario = r,
                asunto = asunto,
                cuerpo = cuerpo,
            )
            if parent_msg is not None:
                msg.parent_msg = parent_msg
                parent_msg.respondido_el = timezone.now()
                parent_msg.save()
            msg.save()
            mensaje_list.append(msg)            
        return mensaje_list
