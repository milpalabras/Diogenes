from django.urls import path


from .views import Editarprofile, cambiar_password, login_view, register_user, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile', profile, name='profile'),
    path('editar_profile', Editarprofile, name='editar_profile'),
    path('cambiar_password', cambiar_password, name='cambiar_password'),
    
]
