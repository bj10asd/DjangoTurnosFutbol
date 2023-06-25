from django.shortcuts import render
from django.urls import path
from canchas.models import Cancha


def index(request):
    cancha = Cancha.objects.all()
    return render(request,'index.html',{'canchas':cancha})

def login(request):
    #pass
    return render(request, 'login.html',{})