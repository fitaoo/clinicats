# Generated by Django 5.2.3 on 2025-07-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_empleado_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='posts_blog/')),
                ('publicado', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='empleados/'),
        ),
    ]
