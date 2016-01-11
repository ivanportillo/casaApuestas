# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0002_auto_20151217_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='fechaNacimiento',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
