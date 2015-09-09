# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('respite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('initial', models.CharField(max_length=1, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('stay_reason', models.TextField(max_length=500)),
                ('stay_start_date', models.DateField(default=datetime.date.today, verbose_name='Start date')),
                ('stay_end_date', models.DateField(null=True, verbose_name='End date', blank=True)),
                ('housing_status', models.TextField(max_length=300, blank=True)),
                ('employment_status', models.TextField(max_length=300, blank=True)),
                ('other_notes', models.TextField(max_length=1000, blank=True)),
                ('referrer', models.CharField(max_length=30, blank=True)),
                ('patient', models.ForeignKey(to='respite.Patient')),
            ],
        ),
    ]
