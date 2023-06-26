from django.urls import path
from canchas import views

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.deslogearse , name='logout'),

    #Cancha
    path('canchas/', views.CanchasListView.as_view() , name='canchas'),
]