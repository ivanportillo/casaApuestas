# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participacion',
            options={'verbose_name_plural': 'Participaciones'},
        ),
        migrations.AlterModelOptions(
            name='perfilusuario',
            options={'verbose_name_plural': 'Perfiles de usuario'},
        ),
        migrations.AddField(
            model_name='apuesta',
            name='fechaFin',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='fechaInicio',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
