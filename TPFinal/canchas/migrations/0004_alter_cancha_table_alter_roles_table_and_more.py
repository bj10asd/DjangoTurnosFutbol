# Generated by Django 4.1 on 2023-06-26 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0003_alter_turnos_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cancha',
            table='cancha',
        ),
        migrations.AlterModelTable(
            name='roles',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='roles_users',
            table='roles_users',
        ),
        migrations.AlterModelTable(
            name='turnos',
            table='turnos',
        ),
    ]