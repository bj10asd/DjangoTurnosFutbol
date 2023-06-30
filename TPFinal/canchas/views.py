from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from canchas.models import Cancha,Roles_Users,Roles,Turnos
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from canchas.forms import TurnosForm

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

def registrarse(request):
    #pass
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        e = request.POST.get('email')
        rdo = User.objects.filter(email=e).count()
        if rdo > 0:
            messages.error(request, 'El email proporcionado ya está en uso')
            return redirect('registro')
        else:
            u = request.POST.get('username')
            p = request.POST.get('password')
            user = User.objects.create_user(u,e,p)
            if user:
                if request.POST.get('switch') == 'on':
                    #print("QUIERE SER CANCHERO")
                    DarRol(user,'Canchero')
                else:
                    #print('QUIERE JUGAR A LA PELOTA')
                    DarRol(user,"Jugador")
                user.first_name = request.POST.get('nombre')
                user.last_name  = request.POST.get('apellido') or ''
                user.save() 
                login(request,user)
                messages.success(request, 'Registro completo, bienvenido {}'.format(user.first_name)+' '+format(user.last_name))
                return redirect('index')
            else:
                print('nose pudo')
    return render(request,'registro.html',{})

def DarRol(user,rol):
    nuevo_ru = Roles_Users()
    nuevo_ru.user_id = user
    nuevo_ru.rol_id  = Roles.objects.get(descripcion=rol)
    nuevo_ru.save()

def canchas(request):
    """cancha = Cancha.objects.all()
    return render(request,'canchas.html',{'canchas':cancha})"""

class CanchasListView(ListView):
    model               = Cancha
    context_object_name = 'canchas'
    template_name       = 'canchas.html'

    def get_queryset(self): 
        rta = Cancha.objects.all()
        filtro = self.get_ObtenerFiltro()
        if filtro:
            rta1 = rta.filter(user_id__in=User.objects.filter(first_name__icontains=filtro).values('id'))
            rta2 = rta.filter(nombre__icontains=filtro)
            rta  = rta1.union(rta2)
            
        return rta

    def get_ObtenerFiltro(self):
        return self.request.GET.get('q') or ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.get_ObtenerFiltro()
        return context

    

import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView

class POIsMapView(TemplateView):
    #https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html
    template_name = 'mapa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pois = Cancha.objects.all()
        lista = []

        for poi in pois:
            json_dict = {}
            json_dict['type']       = 'Feature'
            json_dict['properties'] = dict(name=poi.user_id.first_name)#poi.nombre
            json_dict['geometry']   = dict(type='Point',coordinates = list([poi.lat,poi.lng]))
            lista.append(json_dict)
        
        context['markers'] = lista
        return context


#def calendario(request):
    """todosTurnos = Turnos.objects.all()
    print(todosTurnos.values_list())
    context = {
        'turnos' : todosTurnos
    }
    return render(request,'horarios.html',context)"""

class calendarioLV(ListView):
#https://github.com/sajib1066/event-calendar/blob/main/calendarapp/urls.py

    model               = Turnos
    template_name       = 'horarios.html'
    context_object_name = 'turnos'

    def get_queryset(self):
        #return super().get_queryset() self.kwargs['studentId']
        #print(self.kwargs['pk'])
        return Turnos.objects.filter(id = self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        #print(self.get_queryset()) cancha.user_id.first_name
        var =Cancha.objects.get(id = self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        print(var.user_id.first_name)
        context['cancha'] = var.user_id.first_name
        return context

"""def create_event(request):
    form = TurnosForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
        )
        user_id = form.cleaned_data["user_id"]
        cancha_id = form.cleaned_data["cancha_id"]
        fecha_ini = form.cleaned_data["fecha_ini"]
        fecha_fin = form.cleaned_data["fecha_fin"]
        Turnos.objects.create(user_id,cancha_id,fecha_ini,fecha_fin)
        #return HttpResponseRedirect(reverse("calendarapp:calendar"))
        messages.success(request, 'Se reservó su cancha')
        return redirect('index')
    return render(request, "horarios.html", {"form": form})"""

def create_turno(request):
    pass

def nuevoh(request):
    return render(request,'nuevoh.html',{})