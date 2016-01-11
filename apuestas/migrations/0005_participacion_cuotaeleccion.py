# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0004_remove_deporte_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='participacion',
            name='cuotaEleccion',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
