from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Categorias, DraggableMPTTAdmin)
admin.site.register(Registros)
admin.site.register(Forma_de_pago)
admin.site.register(Etiqueta)
admin.site.register(Cuenta)