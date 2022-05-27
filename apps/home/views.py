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
    
    context = {'cuentas':cuentas,
                #'totalG':round(totalanualG['total'],2),
                #'totalI':round(totalanualI['total'], 2),
                'profile':profile   
    
                }

    return render(request, 'home/index.html', context)
    





