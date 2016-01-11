# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('opcion1', models.CharField(max_length=200)),
                ('cuotaOpcion1', models.FloatField(default=0)),
                ('opcion2', models.CharField(max_length=200)),
                ('cuotaOpcion2', models.FloatField(default=0)),
                ('opcion3', models.CharField(max_length=200)),
                ('cuotaOpcion3', models.FloatField(default=0)),
                ('opcionGanadora', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to=b'imgDeportes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eleccion', models.PositiveSmallIntegerField()),
                ('cantidad', models.FloatField()),
                ('apuesta', models.ForeignKey(to='apuestas.Apuesta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='perfilUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dinero', models.FloatField(default=0)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participacion',
            name='usuario',
            field=models.ForeignKey(to='apuestas.perfilUsuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='deporte',
            field=models.ForeignKey(to='apuestas.Deporte'),
            preserve_default=True,
        ),
    ]
