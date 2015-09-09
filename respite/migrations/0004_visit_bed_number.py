# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respite', '0003_auto_20150831_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='bed_number',
            field=models.IntegerField(default=0),
        ),
    ]
