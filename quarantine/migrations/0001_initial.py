# Generated by Django 3.0.5 on 2020-05-03 16:19

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
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000, unique=True)),
                ('descrição', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_data', models.DateTimeField(verbose_name='data de publicacao')),
                ('titulo', models.CharField(max_length=1000)),
                ('conteudo', models.CharField(max_length=10000)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quarantine.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='MembroGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarantine.Grupo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='membros',
            field=models.ManyToManyField(through='quarantine.MembroGrupo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=10000)),
                ('karma', models.IntegerField(verbose_name='votos')),
                ('pub_data', models.DateTimeField(verbose_name='data de comentario')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarantine.Publicacao')),
            ],
        ),
    ]
