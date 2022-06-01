
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, ProfileForm, CambiarpasswordForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from finanzas.models import Cuenta, Categorias
from django.core import management
# Create your views here.

def login_view(request):
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)                                
                return redirect("/")
            else:
                msg = 'Credenciales invalidas, vuelva a intentar'
        else:
            msg = 'Error al cargar los datos. Revise su usuario y contraseña'
    
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            success = True
            messages.success(request, f"Nueva cuenta creada: {username}" )
            cuenta_inicial=Cuenta.objects.all()
            categorias_inicial=Categorias.objects.all()
            if (not cuenta_inicial):                
                cuenta_inicial = Cuenta(nombre="Cuenta Inicial", monto=0, tipo_de_cuenta="GRAL")
                cuenta_inicial.save()
            if (not categorias_inicial):
               management.call_command('loaddata', 'categorias.json')
            
            msg = 'Usuario creado - Dirigase al <a href="/login">login</a>.'
            
            return redirect("/login/")

        else:
            msg = 'Revise sus datos'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

@login_required
def profile (request):
    profile, __ = Profile.objects.get_or_create(user=request.user)
    return render (request, 'accounts/perfil.html', {'profile': profile})

@login_required
def Editarprofile (request):
    profile, __ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)       
        if form.is_valid():
                profile = form.save()                
                profile.user.first_name = form.cleaned_data.get('first_name')
                profile.user.last_name = form.cleaned_data.get('last_name')
                profile.user.email = form.cleaned_data.get('email')                
                profile.user.save()
                messages.success(request, 'Perfil guardado satisfactoriamente')        
                return redirect('/profile')
        else:
            messages.error(request, 'Error al guardar el perfil, revise sus datos')
    else:
        form = ProfileForm(instance=profile)        
    return render (request, 'accounts/editar_perfil.html', {'ProfileForm':form, 'profile':profile})

@login_required
def cambiar_password(request):
    usuario = request.user    
    if request.method == 'POST':
        form = CambiarpasswordForm(request.POST)
        if form.is_valid():            
            usuario.set_password(form.cleaned_data.get('password1'))
            usuario.save()
            messages.success(request, 'Contraseña cambiada satisfactoriamente, debera ingresar nuevamente')
            return redirect('/login')
    else:
        form = CambiarpasswordForm(instance=request.user)
    return render(request, 'accounts/cambiar_password.html', {'form': form})
