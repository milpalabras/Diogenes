from django.shortcuts import redirect, render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from mensajeria.models import Mensaje
from mensajeria.forms import ComposeForm
from mensajeria.utils import format_quote, get_user_model, get_username_field

User = get_user_model()



@login_required
def inbox(request):
    mensaje_list = Mensaje.objects.inbox_user(request.user)
    return render(request, 'mensajeria/inbox.html', {'mensaje_list': mensaje_list })

@login_required
def outbox(request):    
    mensaje_list = Mensaje.objects.salida_user(request.user)
    return render(request, 'mensajeria/outbox.html', {'mensaje_list': mensaje_list})

@login_required
def trash(request):    
    mensaje_list = Mensaje.objects.papelera_user(request.user)
    return render(request, 'mensajeria/trash.html', {
        'mensaje_list': mensaje_list,
    })

@login_required
def redactar(request, recipient=None,recipient_filter=None):
   
    if request.method == "POST":
        remitente = request.user
        form = ComposeForm(request.POST, recipient_filter=recipient_filter)
        if form.is_valid():
            form.save(remitente=request.user)
            messages.success(request, "Mensaje enviado correctamente.")            
            return redirect('messages_inbox')
    else:
        form = ComposeForm(initial={"asunto": request.GET.get("asunto", "")})
        if recipient is not None:
            recipients = [u for u in User.objects.filter(**{'%s__in' % get_username_field(): [r.strip() for r in recipient.split('+')]})]
            form.fields['recipient'].initial = recipients
    return render(request, 'mensajeria/compose.html', {'form': form})

@login_required
def reply(request, pk,          
        recipient_filter=None, quote_helper=format_quote,
        asunto_re=_(u"Re: %(subject)s"),):
    """
    Prepares the ``form_class`` form for writing a reply to a given message
    (specified via ``message_id``). Uses the ``format_quote`` helper from
    ``messages.utils`` to pre-format the quote. To change the quote format
    assign a different ``quote_helper`` kwarg in your url-conf.

    """
    parent = get_object_or_404(Mensaje, id=pk)

    if parent.remitente != request.user and parent.destinatario != request.user:
        raise Http404

    if request.method == "POST":
        remitente = request.user
        form = ComposeForm(request.POST, recipient_filter=recipient_filter)
        if form.is_valid():
            form.save(remitente=request.user, parent_msg=parent)
            messages.success(request, "Mensaje enviado correctamente.")           
            return render('messages_inbox')
    else:
        form = ComposeForm(initial={
            'cuerpo': quote_helper(parent.remitente, parent.cuerpo),
            'asunto': asunto_re % {'subject': parent.asunto},
            'destinatario': [parent.remitente,]
            })
    return render(request, 'mensajeria/compose.html', {'form': form})

@login_required
def delete(request, message_id):    
    user = request.user
    now = timezone.now()
    mensaje = get_object_or_404(Mensaje, id=message_id)
    deleted = False   
    if mensaje.remitente == user:
        mensaje.remitente_borrado_el = now
        deleted = True
    if mensaje.destinatario == user:
        mensaje.destinatario_borrado_el = now
        deleted = True
    if deleted:
        mensaje.save()
        messages.success(request,"Mensaje eliminado correctamente.")        
        return redirect('messages_inbox')
    raise Http404

@login_required
def undelete(request, message_id):    
    user = request.user
    mensaje = get_object_or_404(Mensaje, id=message_id)
    undeleted = False       
    if mensaje.remitente == user:
        mensaje.remitente_borrado_el = None
        undeleted = True
    if mensaje.destinatario == user:
        mensaje.destinatario_borrado_el = None
        undeleted = True
    if undeleted:
        mensaje.save()
        messages.success(request, "Mensaje restaurado correctamente.")
        success_url = reverse('messages_inbox')        
        return HttpResponseRedirect(success_url)
    raise Http404

@login_required
def view(request, message_id, quote_helper=format_quote,
        asunto_re=_(u"Re: %(subject)s"),
        ):
    """
    Shows a single message.``message_id`` argument is required.
    The user is only allowed to see the message, if he is either
    the sender or the recipient. If the user is not allowed a 404
    is raised.
    If the user is the recipient and the message is unread
    ``read_at`` is set to the current datetime.
    If the user is the recipient a reply form will be added to the
    tenplate context, otherwise 'reply_form' will be None.
    """
    user = request.user
    now = timezone.now()
    mensaje = get_object_or_404(Mensaje, pk=message_id)
    if (mensaje.remitente != user) and (mensaje.destinatario != user):
        raise Http404
    if mensaje.leido_el is None and mensaje.destinatario == user:
        mensaje.leido_el = now
        mensaje.save()

    context = {'mensaje': mensaje, 'reply_form': None}
    if mensaje.destinatario == user:
        form = ComposeForm(initial={
            'cuerpo': quote_helper(mensaje.remitente, mensaje.cuerpo),
            'asunto': asunto_re % {'subject': mensaje.asunto},
            'destinatario': [mensaje.remitente,]
            })
        context['reply_form'] = form
    return render(request, 'mensajeria/view.html', context)
