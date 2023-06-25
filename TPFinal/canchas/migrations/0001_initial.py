# Generated by Django 4.1 on 2023-06-23 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('foto', models.CharField(db_column='Foto', max_length=250)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=250, null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'Cancha',
                'verbose_name_plural': 'Canchas',
                'db_table': 'Cancha',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ini', models.DateTimeField(db_column='Fecha_Ini')),
                ('fecha_fin', models.DateTimeField(db_column='Fecha_Fin')),
                ('cancha_id', models.ForeignKey(db_column='cancha_id', on_delete=django.db.models.deletion.PROTECT, to='canchas.cancha')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'db_table': 'Turnos',
                'ordering': ['cancha_id'],
            },
        ),
    ]