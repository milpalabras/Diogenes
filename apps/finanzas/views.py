
from decimal import Decimal
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import Gastosform, Ingresosform, Editarform,  Cuentaform, Categoriaform
from .models import Categorias, Cuenta, Registros
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#---------CRUD Registros-----------------
@login_required
def registros(request):
    return render (request, 'finanzas/registros.html')

@login_required
def Cargargastos (request):
    if request.method == 'POST':
        form = Gastosform(request.POST, request.FILES)
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

@login_required
def Cargaringresos (request):
    if request.method == 'POST':
        form = Ingresosform(request.POST, request.FILES)
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

@login_required
def EliminarRegistro(request, pk):
    registro = Registros.objects.get(pk=pk)
    importe = registro.importe
    cuenta = registro.cuenta_id
    if cuenta != None:
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
    else:
        registro.delete()
        return redirect('registros')  

@login_required
def EditarRegistro(request, pk):
    registro = get_object_or_404(Registros, pk=pk)
    tipo = registro.tipo_de_registro
    importe_actual = Decimal(registro.importe)
   
    if request.method == 'POST':
        form = Editarform(request.POST, request.FILES, instance=registro)
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

class RegistrosList(LoginRequiredMixin,ListView):
    model = Registros
    template_name = 'finanzas/registros.html'

class RegistroDetalle(LoginRequiredMixin,DetailView):
    model = Registros
    template_name = 'finanzas/registro_detalle.html'

#---------CRUD Cuenta-----------------
class CuentasList(LoginRequiredMixin,ListView):
    model = Cuenta
    template_name = 'finanzas/cuentas.html'

class CuentaDetalle(LoginRequiredMixin,DetailView):
    model = Cuenta
    template_name = 'finanzas/cuenta_detalle.html'

class crearcuenta (LoginRequiredMixin,CreateView):
    model = Cuenta
    success_url= "cuentas"
    fields= "__all__"    

class Editarcuenta (LoginRequiredMixin,UpdateView):
    model = Cuenta
    success_url= "/cuentas"
    form_class = Cuentaform

@login_required
def Eliminarcuenta (request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    cuenta.delete()
    return redirect('/cuentas')

#---------CRUD Categoria-----------------
@login_required
def CategoriaList(request):
    categorias = Categorias.objects.filter(parent__isnull=True)
    if request.method == 'POST':
        form = Categoriaform(request.POST)
        if form.is_valid():
            messages.success(request, "Categoria creada")
            form.save()
            return redirect('/')
    else:
        form = Categoriaform()       
    return render (request, 'finanzas/categorias.html',{'categorias':categorias, 'form':form})
    
class Eliminarcategoria (LoginRequiredMixin,DeleteView):
    model = Categorias
    success_url= "/categorias"

@login_required
def Crearsubcategoria (request):
    if request.method == 'POST':
        form = Categoriaform(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.parent = request.POST['parent']
            categoria.save()
            return redirect('/')
    else:
        form = Categoriaform()
    return render (request, 'includes/modal_cargarcategoria.html', {'form':form})

class Editarsubcategoria (LoginRequiredMixin,UpdateView):
    model = Categorias
    success_url= "/categorias"
    form_class = Categoriaform