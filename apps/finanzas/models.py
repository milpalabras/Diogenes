from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from colorfield.fields import ColorField
from datetime import date
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Cuenta (models.Model):
    nombre = models.CharField(max_length=30)
    color = ColorField(default='#FF0000', blank = True, null=True)
    class tipodecuenta (models.TextChoices):
        GENERAL = 'GRAL', _('General')
        EFECTIVO ='EFEC', _('Efectivo')
        BANCARIA = 'BANC', _('Cuenta Bancaria')
        CREDITO = 'CRED', _('Tarjeta de Credito')
        AHORRO = 'AHOR', _('Cuenta de ahorros')
        EXTRA = 'EXTR', _('Extra')
        SEGURO = 'SEGU', _('Seguro')
        INVERSION = 'INVE', _('Inversión')
        PRESTAMO = 'PRES', _('Prestamo')
        HIPOTECA = 'HIPO', _('Hipoteca')
    tipo_de_cuenta = models.CharField(max_length=4, choices=tipodecuenta.choices, default=tipodecuenta.GENERAL)
    monto= models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural="Cuentas"
    
    def __str__(self):
        return self.nombre


class Categorias (MPTTModel):
    nombre = models.CharField(max_length=30)
    parent = TreeForeignKey ('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    icon = models.ImageField(upload_to='icon_categoriagastos', null=True, blank=True)
    color = ColorField(default='#FF0000')    
    class Tipodegasto (models.TextChoices):
        FIJO ='F', _('Fijo-Obligatorio')
        NECESIDAD = 'N', _('Necesario-Sobrevivencia')
        PRESCINDIBLE = 'P',_('Prescindible-Lujo')       
    
    tipo_de_gasto = models.CharField(max_length=1, choices=Tipodegasto.choices, default=Tipodegasto.FIJO)

    class MPTTMeta:
        order_insertion_by=['nombre']

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

    

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name_plural="Etiquetas"

    def __str__(self):
        return self.nombre


class Forma_de_pago(models.Model):
    nombre = models.CharField(max_length=350)

    class Meta:
        verbose_name_plural="Forma de pagos"
    
    def __str__(self):
        return self.nombre


class Registros (models.Model):
    class Tiporegistro (models.TextChoices):
        GASTO = 'GAST', _('Gasto')
        INGRESO ='INGR', _('Ingreso')
        TRANSFERENCIA = 'TRAN', _('Transferencia')
    tipo_de_registro = models.CharField(max_length=4, choices=Tiporegistro.choices, default=Tiporegistro.GASTO)
    importe = models.DecimalField(max_digits=15,  decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    nota = models.CharField(max_length=100, blank=True, null=True)
    fecha_de_pago = models.DateField(default=date.today)
    categoria = models.ForeignKey("Categorias", on_delete=models.CASCADE)
    cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE)
    etiqueta = models.ForeignKey('Etiqueta',on_delete=models.CASCADE, null=True, blank=True )
    forma_de_pago = models.ForeignKey('Forma_de_pago', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.tipo_de_registro