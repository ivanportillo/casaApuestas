# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0007_auto_20160109_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='fechaFin',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
