# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0006_remove_apuesta_opcionganadora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apuesta',
            name='fechaFin',
        ),
        migrations.RemoveField(
            model_name='apuesta',
            name='fechaInicio',
        ),
    ]
