import re
import django
from django.utils.text import wrap
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.conf import settings

# favour django-mailer but fall back to django.core.mail



def format_quote(remitente, cuerpo):
    """
    Wraps text at 55 chars and prepends each
    line with `> `.
    Used for quoting messages in replies.
    """
    lines = wrap(cuerpo, 55).split('\n')
    for i, line in enumerate(lines):
        lines[i] = "> %s" % line
    quote = '\n'.join(lines)
    return _(u"%(remitente)s escribio:\n%(cuerpo)s") % {
        'remitente': remitente,
        'cuerpo': quote
    }

def get_user_model():
    if django.VERSION[:2] >= (1, 5):
        from django.contrib.auth import get_user_model
        return get_user_model()
    else:
        from django.contrib.auth.models import User
        return User


def get_username_field():
    if django.VERSION[:2] >= (1, 5):
        return get_user_model().USERNAME_FIELD
    else:
        return 'username'
