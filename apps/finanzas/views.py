
from decimal import Decimal
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .forms import Gastosform, Ingresosform, Editarform,  Cuentaform, Categoriaform
from .models import Categorias, Cuenta, Registros
from django.views.generic import ListView, DetailView

# Create your views here.

def registros(request):
    return render (request, 'finanzas/registros.html')

def Cargargastos (request):
    if request.method == 'POST':
        form = Gastosform(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.tipo_de_registro = 'GAST'
            categoria = form.cleaned_data.get('categoria')
            importe = form.cleaned_data.get('importe')            
            cuenta_id = request.POST['cuenta']
            cuenta = Cuenta.objects.get(pk=cuenta_id)
            cuenta.monto -= importe
            messages.success(request, f"El gasto de la categoria {categoria} con el importe ${importe} ha sido guardado")
            cuenta.save()
            gasto.save()
            return redirect('/')
    else:
        form = Gastosform()
    context = {
        'formgastos': form
    }
     
    return render (request, 'layouts/base.html', context)

def Cargaringresos (request):
    if request.method == 'POST':
        form = Ingresosform(request.POST)
        if form.is_valid(): 
            ingreso = form.save(commit=False)
            ingreso.tipo_de_registro = 'INGR'
            categoria = form.cleaned_data.get('categoria')
            importe = form.cleaned_data.get('importe')             
            cuenta_id = request.POST['cuenta']
            cuenta = Cuenta.objects.get(pk=cuenta_id)
            cuenta.monto += importe
            messages.success(request, f"El ingreso de la categoria {categoria} con el importe ${importe} ha sido guardado")
            cuenta.save()               
               #monto_actual = Cuenta.objects.values_list('monto', flat=True).get(pk=cuenta_id)
               #cuenta_actualizado = Cuenta(pk=cuenta_id, monto=(monto_actual + importe) )
               #cuenta_actualizado.save()  
            ingreso.save() 
            return redirect('/')              
    else:
        form = Ingresosform()
    context = {
        'formingresos': form
    }
    return render (request, 'layouts/base.html', context)


def EliminarRegistro(request, pk):
    registro = Registros.objects.get(pk=pk)
    importe = registro.importe
    cuenta = registro.cuenta_id
    monto = Cuenta.objects.get(pk=cuenta)
    tipo = registro.tipo_de_registro
    if tipo == 'GAST' :
        monto.monto += importe
        monto.save()
        registro.delete()
        
        return redirect ('registros')
    else:
        monto.monto -= importe
        monto.save()
        registro.delete()
        return redirect('registros')   
    

    return redirect('/registros')


def EditarRegistro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    tipo = registro.tipo_de_registro
    importe_actual = Decimal(registro.importe)
   
    if request.method == 'POST':
        form = Editarform(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.importe = request.POST['importe']
            registro.cuenta_id =request.POST['cuenta']
            registro.fecha_de_pago = request.POST['fecha_de_pago']
            registro.nota = request.POST['nota']
            registro.categoria_id = request.POST['categoria']
            cuenta = Cuenta.objects.get(pk=registro.cuenta_id)
            importe_nuevo = Decimal(registro.importe)
            if tipo == 'GAST' :
                if importe_actual > importe_nuevo:
                    diferencia = importe_actual - importe_nuevo
                    cuenta.monto += diferencia
                elif importe_actual < importe_nuevo:
                    diferencia = importe_nuevo - importe_actual
                    cuenta.monto -= diferencia                
            else:
                if importe_actual > importe_nuevo:
                    diferencia = importe_actual - importe_nuevo
                    cuenta.monto -= diferencia
                elif importe_actual < importe_nuevo:
                    diferencia = importe_nuevo - importe_actual
                    cuenta.monto += diferencia 
            
            cuenta.save()
            registro.save()
            
            return redirect('registros')            
    else:
        form=Editarform (instance=registro)
        context = {'form': form,  'pk':pk }
    

    return render (request, 'finanzas\editar_registro.html', context)

class RegistrosList(ListView):
    model = Registros
    template_name = 'finanzas/registros.html'

class RegistroDetalle(DetailView):
    model = Registros
    template_name = 'finanzas/registro_detalle.html'


class CuentasList(ListView):
    model = Cuenta
    template_name = 'finanzas/cuentas.html'

class CuentaDetalle(DetailView):
    model = Cuenta
    template_name = 'finanzas/cuenta_detalle.html'

def crearcuenta (request):
    if request.method == 'POST':
        form = Cuentaform(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            messages.success(request, f"Nueva cuenta creada: {nombre}" )               
            form.save()
            return redirect('/')               
    else:          
        form = Cuentaform()
    context = {'formcuentas': form}
    return render(request, 'home/index.html', context)

def Editarcuenta (request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == 'POST':
        form = Cuentaform(request.POST, instance=cuenta)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            messages.success(request, f"Cuenta modificada {nombre}" )               
            form.save()
            return redirect('/')               
    else:          
        form = Cuentaform(instance=cuenta)
    context = {'formcuentas': form}
    return render(request, 'finanzas/cuentas.html', context)

def Eliminarcuenta (request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    cuenta.delete()
    return redirect('/')

def Crearsubcategoria (request):     
     categorias = Categorias.objects.filter(parent__isnull=True)
     if request.method == 'POST':
          form = Categoriaform(request.POST)
          if form.is_valid():               
               form.save()
               return redirect('/')
     else:
          form = Categoriaform()
     return render (request, 'finanzas/categorias.html',{'form':form, 'categorias':categorias})
