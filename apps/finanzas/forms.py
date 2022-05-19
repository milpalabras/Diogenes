from django import forms
from .models import Categorias, Registros, Cuenta
#---------------------------------------------------------------------------------------------------------------

class Gastosform(forms.ModelForm):

    class Meta:
        model = Registros
        fields = ('importe', 'cuenta', 'fecha_de_pago', 'nota', 'categoria' )
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de pago', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
        }


class Ingresosform(forms.ModelForm):    

    class Meta:
        model = Registros
        fields = ('importe', 'cuenta', 'fecha_de_pago', 'nota', 'categoria')
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Cuentaform (forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('nombre', 'monto', 'tipo_de_cuenta' )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_de_cuenta': forms.Select(attrs={'class': 'form-control'}),
        }

        labels ={
            'nombre': "Nombre de la cuenta", 
            'monto': "Monto inicial de la cuenta",
            'tipo_de_cuenta':'Seleccione el tipo de cuenta'
        }


class Categoriaform (forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Categorias.objects.filter(parent__isnull=True), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'}))    

    class Meta:
        model = Categorias
        fields = ('nombre', 'parent', 'tipo_de_gasto')
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'}),
            'tipo_de_gasto': forms.Select(attrs={'class': 'form-control'}),
        }

        labels ={
            'nombre': "Nombre de la categoria", 
            'parent': "Categoria Padre"
        }


class Editarform(forms.ModelForm):

    class Meta:
        model = Registros
        fields = ('importe', 'cuenta', 'fecha_de_pago', 'nota', 'categoria' )
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de pago', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
        }