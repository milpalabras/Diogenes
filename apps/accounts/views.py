
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, ProfileForm
from django.contrib import messages
from .models import Profile
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
                msg = 'Credenciales invalidas'
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
            msg = 'Usuario creado - Dirigase al <a href="/login">login</a>.'
            
            return redirect("/login/")

        else:
            msg = 'Revise sus datos'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def profile (request):
    return render (request, 'accounts/perfil.html')

def Editarprofile (request):
    profile, __ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
                profile = form.save()
                profile.first_name = form.cleaned_data.get('first_name')
                profile.last_name = form.cleaned_data.get('last_name')
                profile.email = form.cleaned_data.get('email')
                profile.save()
                messages.success(request, 'Perfil guardado satisfactoriamente')        
        return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render (request, 'accounts/perfil.html', {'ProfileForm':form, 'profile':profile})