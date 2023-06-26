from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from canchas.models import Cancha
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    #cancha = Cancha.objects.all()
    return render(request,'index.html',{})#,{'canchas':cancha})

def login_view(request):
    #pass
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        user = request.POST.get('username')
        pw   = request.POST.get('password')
        us = authenticate(username=user,password=pw)#authenticate solo si existe o no en la bd
        if us:
            login(request,us)
            messages.success(request, 'Bienvenido {}'.format(us.first_name)+' '+format(us.last_name))
            print('Bienvenido {}'.format(us.get_username()))
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña invalidos")
            return redirect('login')

    return render(request, 'login.html',{})

def deslogearse(request):
    logout(request)
    return redirect('index')

def canchas(request):
    """cancha = Cancha.objects.all()
    return render(request,'canchas.html',{'canchas':cancha})"""

class CanchasListView(ListView):
    model = Cancha
    context_object_name = 'canchas'
    template_name = 'canchas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context