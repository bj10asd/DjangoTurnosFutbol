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
    path('canchas/map/<int:pk>/', views.POIsMapView.as_view() , name='mapa'),

    #HORARIOS DE CANCHAS 
    path('canchas/horario/<int:pk>', views.calendarioLV.as_view() , name='calendario'),

    #Turnos
    #ath('canchas/horario/new', views.create_event , name='crear_turno'),
    path('canchas/horario/new/<int:pk>', views.create_turno , name='crear_turno'),

    #PDF
    path('pdf_view/', views.ViewPDF.as_view(), name='pdf_view'),
    

    path('canchas/nuevo', views.nuevoh , name='n'),
]