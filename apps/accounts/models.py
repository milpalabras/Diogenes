from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.

class Profile(models.Model): 

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)    
    celular = models.CharField(max_length=32, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    altura = models.CharField(max_length=32, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)    
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    cod_postal = models.CharField(max_length=30, null=True, blank=True)
    sobre_mi = models.CharField(max_length=500, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuarios'

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/default-profile-picture.png')