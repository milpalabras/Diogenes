from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from finanzas.models import Registros, Cuenta
from django.db.models import Sum
from datetime import date, datetime

# Create your views here.

@login_required(login_url="/login/")
def index(request):
    now=datetime.now()
    cuentas = Cuenta.objects.all()
    #gastos_mensuales_total=Registros.objects.filter(fecha_de_pago__month=now.month).aggregate(total=Sum('importe'))
    #ingresos_mensuales_total=Registros.objects.filter(fecha_de_ingreso__month=now.month).aggregate(total=Sum('importe'))
    context = {'cuentas':cuentas}

    return render(request, 'home/index.html', context)
    #{       
     #   'gastos_mensuales':gastos_mensuales_total['total'], 
      #  'ingresos_mensuales': ingresos_mensuales_total['total']})






