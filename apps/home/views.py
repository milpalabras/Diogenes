from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from finanzas.models import Registros, Cuenta
from django.db.models import Sum
from datetime import date, datetime
from accounts.models import Profile

# Create your views here.

@login_required(login_url="/login/")
def index(request):
    profile, __ = Profile.objects.get_or_create(user=request.user)
    now=datetime.now()
    cuentas = Cuenta.objects.all()
    totalanualG=Registros.objects.filter(fecha_de_pago__year=now.year).filter(tipo_de_registro="GAST").aggregate(total=Sum('importe'))
    totalanualI=Registros.objects.filter(fecha_de_pago__year=now.year).filter(tipo_de_registro="INGR").aggregate(total=Sum('importe'))
    totalmensualI=Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="INGR").aggregate(total=Sum('importe'))
    contTOTAL=(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="INGR").filter(categoria__tipo_de_categoria='I').count())
    context = {'cuentas':cuentas,
                'totalG':totalanualG['total'],
                'totalI':totalanualI['total'],
                'totalmensualI':totalmensualI['total'], 
                'contTOTAL':contTOTAL,
                'profile':profile   
    
                }

    return render(request, 'home/index.html', context)

def acerca_de_mi(request):
    return render(request, 'home/acerca_de_mi.html')
    





