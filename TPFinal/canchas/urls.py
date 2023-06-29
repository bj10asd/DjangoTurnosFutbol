from django.urls import path
from canchas import views

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.deslogearse , name='logout'),
    path('register/', views.registrarse , name='registro'),

    #Cancha
    path('canchas/', views.CanchasListView.as_view() , name='canchas'),
    path('canchas/map', views.POIsMapView.as_view() , name='mapa'),

    #HORARIOS DE CANCHAS 
    path('canchas/horario', views.calendarioLV.as_view() , name='calendario'),

    path('canchas/nuevo', views.nuevoh , name='mapa'),
]