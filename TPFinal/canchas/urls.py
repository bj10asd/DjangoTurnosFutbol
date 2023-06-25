from django.urls import path
from canchas import views

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]