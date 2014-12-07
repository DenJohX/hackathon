# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.TextField(blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('titulo', models.TextField(blank=True)),
                ('direccion', models.TextField()),
                ('foto', models.ImageField(upload_to=b'')),
                ('categoria', models.CharField(max_length=80, blank=True)),
                ('historia', models.TextField()),
                ('inicia', models.DateTimeField(null=True, blank=True)),
                ('recaudado', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('voluntarios', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
