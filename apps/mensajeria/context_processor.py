from mensajeria.models import inbox_count, mensajes_sin_leer

def _user_is_authenticated(user):   
        return user.is_authenticated

def inbox(request): 
        if _user_is_authenticated(request.user):      
                return {'messages_inbox_count': inbox_count(request.user)}
        else:
                return {}
        

def mensaje_sin_leer(request):
        if _user_is_authenticated(request.user):    
                return {'mensajes_sin_leer': mensajes_sin_leer(request.user)}
        else:
                return {}
  
