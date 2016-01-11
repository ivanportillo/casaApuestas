# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0005_participacion_cuotaeleccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apuesta',
            name='opcionGanadora',
        ),
    ]
