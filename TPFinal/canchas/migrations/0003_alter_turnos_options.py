# Generated by Django 4.1 on 2023-06-26 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0002_roles_alter_cancha_foto_roles_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turnos',
            options={'ordering': ['id', 'cancha_id'], 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
    ]
