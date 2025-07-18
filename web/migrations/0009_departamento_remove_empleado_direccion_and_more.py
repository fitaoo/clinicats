# Generated by Django 5.2.3 on 2025-07-09 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='direccion',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatar.png', null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleados', to='web.departamento'),
        ),
    ]
