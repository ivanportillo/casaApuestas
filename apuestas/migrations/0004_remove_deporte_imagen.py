# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0003_perfilusuario_fechanacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='imagen',
        ),
    ]
