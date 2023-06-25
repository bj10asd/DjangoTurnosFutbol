# Generated by Django 4.1 on 2023-06-24 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('canchas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=40)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'db_table': 'Roles',
                'ordering': ['descripcion'],
            },
        ),
        migrations.AlterField(
            model_name='cancha',
            name='foto',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
        migrations.CreateModel(
            name='Roles_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_id', models.ForeignKey(db_column='rol_id', on_delete=django.db.models.deletion.PROTECT, to='canchas.roles', verbose_name='Rol')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'Rol usuario',
                'verbose_name_plural': 'Roles de usuarios',
                'db_table': 'Roles_Users',
                'ordering': ['user_id'],
            },
        ),
    ]