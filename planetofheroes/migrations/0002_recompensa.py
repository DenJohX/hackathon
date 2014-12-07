# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planetofheroes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recompensa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
