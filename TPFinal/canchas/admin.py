from django.contrib import admin
from canchas.models import Cancha,Turnos,Roles,Roles_Users

# Register your models here.
#USER admin
#PW   Josemaria10

class CanchaAdmin(admin.ModelAdmin):
    list_display    = ['id','user_id','nombre','foto','direccion']
    readonly_fields = ['id']
    search_fields   = ['nombre']
    actions = None

admin.site.register(Cancha,CanchaAdmin)

class TurnosAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','fecha_ini','fecha_fin']
    readonly_fields = ['id']
    search_fields = ['user_id']
    actions = None

admin.site.register(Turnos,TurnosAdmin)

class RolesAdmin(admin.ModelAdmin):
    list_display = ['id','descripcion']
    readonly_fields = ['id']
    search_fields = ['descripcion']
    actions = None

admin.site.register(Roles,RolesAdmin)

class Roles_UsersAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','rol_id']
    readonly_fields = ['id']
    search_fields = ['user_id','rol_id']
    actions = None

admin.site.register(Roles_Users,Roles_UsersAdmin)