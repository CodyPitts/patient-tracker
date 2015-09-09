# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respite', '0002_patient_visit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['-stay_start_date']},
        ),
        migrations.AddField(
            model_name='visit',
            name='discharge',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
