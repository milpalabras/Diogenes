from mensajeria.models import inbox_count_for, mensajes_sin_leer

def _user_is_authenticated(user):
    # django < 2.0
    try:
        return user.is_authenticated()
    except TypeError:
        # django >= 2.0
        return user.is_authenticated

def inbox(request):
    if _user_is_authenticated(request.user):
        return {'messages_inbox_count': inbox_count_for(request.user)}
    else:
        return {}

def mensaje_sin_leer(request):
    if _user_is_authenticated(request.user):
        return {'mensajes_sin_leer': mensajes_sin_leer(request.user)}
    else:
        return {}
