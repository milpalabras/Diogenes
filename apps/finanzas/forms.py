from tkinter import Widget
from django import forms
from .models import Categorias, Registros, Cuenta
from django.db.models import Prefetch

#---------------------------------------------------------------------------------------------------------------



class Gastosform(forms.ModelForm):
    

    class Meta:
        model = Registros
        fields = ('importe', 'cuenta', 'fecha_de_pago', 'nota', 'categoria' )
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de pago', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'id':'basic', 'name':'basic'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(Gastosform, self).__init__(*args, **kwargs)
        cat = Categorias.objects.filter(parent__isnull=True).exclude(nombre="Ingreso").order_by('nombre').prefetch_related(Prefetch('children',
                queryset=Categorias.objects.order_by('nombre')))
        
        self.fields['categoria'].choices =[(c.nombre, [
                (self.fields['categoria'].prepare_value(sc),
                    self.fields['categoria'].label_from_instance(sc))
                for sc in c.children.all()
            ]) for c in cat]


class Ingresosform(forms.ModelForm):    

    class Meta:
        model = Registros
        fields = ('importe', 'cuenta', 'fecha_de_pago', 'nota', 'categoria')
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(Ingresosform, self).__init__(*args, **kwargs)
        cat = Categorias.objects.filter(parent__isnull=True).filter(nombre__iexact='Ingreso').prefetch_related(Prefetch('children',
                queryset=Categorias.objects.order_by('nombre')))
        
        self.fields['categoria'].choices =[("", self.fields['categoria'].empty_label)]+ [(c.nombre, [
                (self.fields['categoria'].prepare_value(sc),
                    self.fields['categoria'].label_from_instance(sc))
                for sc in c.children.all()
            ]) for c in cat]


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
    parent = forms.ModelChoiceField(queryset=Categorias.objects.filter(parent__isnull=True), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'}), label='Categoria superior')
    tipo_de_categoria = forms.ChoiceField(choices=(('F','Gasto Fijo (Obligatorio)'), ('N','Gasto Necesario(Sobrevivencia)'), ('P', 'Gasto Prescindible(Lujo)'), ('I', 'Ingreso de dinero')),widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'})) 

    class Meta:
        model = Categorias
        fields = ('nombre', 'parent', 'tipo_de_categoria')
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'}),
            'tipo_de_categoria': forms.Select(attrs={'class': 'form-control'}),
        }

        labels ={
            'nombre': "Nombre de la subcategoria", 
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
    def __init__(self, *args, **kwargs):
        super(Editarform, self).__init__(*args, **kwargs)
        cat = Categorias.objects.filter(parent__isnull=True).prefetch_related(Prefetch('children',
                queryset=Categorias.objects.order_by('nombre')))
        
        self.fields['categoria'].choices =[("", self.fields['categoria'].empty_label)]+ [(c.nombre, [
                (self.fields['categoria'].prepare_value(sc),
                    self.fields['categoria'].label_from_instance(sc))
                for sc in c.children.all()
            ]) for c in cat]