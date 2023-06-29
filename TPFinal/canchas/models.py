from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cancha(models.Model):
    #Cancha_ID GENERADO POR DJANGO
    user_id   = models.ForeignKey(User, models.PROTECT, db_column='user_id',verbose_name='User ID')
    nombre    = models.CharField(db_column='Nombre',max_length=50,null=False)
    foto      = models.ImageField(upload_to='upload/', null=True)#(db_column='Foto',max_length=250)
    direccion = models.CharField(db_column='Direccion',max_length=250,null=True,blank=True)
    lat       = models.FloatField(db_column='lat',blank=True,null=True)
    lng       = models.FloatField(db_column='lng',blank=True,null=True)

    class Meta:
        db_table = 'cancha'
        ordering = ['nombre']
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'
    
    def __str__(self) -> str:
        # super().__str__()
        return self.user_id.first_name+' | '+ self.nombre

class Turnos(models.Model):
    #Turno_ID GENERADO POR DJANGO
    user_id   = models.ForeignKey(User, models.PROTECT, db_column='user_id',verbose_name='User ID')
    cancha_id = models.ForeignKey(Cancha,models.PROTECT,db_column='cancha_id')
    fecha_ini = models.DateTimeField(db_column='Fecha_Ini',null=False,blank=False)
    fecha_fin = models.DateTimeField(db_column='Fecha_Fin',null=False,blank=False)

    class Meta:
        db_table = 'turnos'
        ordering = ['id','cancha_id']
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
    
    def __str__(self) -> str:
        #return super().__str__()
        return str(self.fecha_ini) + ' hasta ' + str(self.fecha_fin)

class Roles(models.Model):
    descripcion = models.CharField(db_column='Descripcion',max_length=40)

    class Meta:
        db_table = 'roles'
        ordering = ['descripcion']
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self) -> str:
        return self.descripcion
        #return super().__str__()
        
class Roles_Users(models.Model):
    user_id = models.ForeignKey(User,models.PROTECT,db_column='user_id',verbose_name='User ID')
    rol_id  = models.ForeignKey(Roles,models.PROTECT,db_column='rol_id',verbose_name='Rol')

    class Meta:
        db_table = 'roles_users'
        ordering = ['user_id']
        verbose_name = 'Rol usuario'
        verbose_name_plural = 'Roles de usuarios'

    def __str__(self) -> str:
        #return super().__str__()
        return str(self.user_id)+ ' - '+str(self.rol_id)