# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respite', '0004_visit_bed_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'permissions': (('can_see_patients', 'Can see patient list and visit information'),)},
        ),
    ]
