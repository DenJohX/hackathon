# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planetofheroes', '0002_recompensa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.TextField(blank=True)),
                ('comentario', models.TextField(blank=True)),
                ('campania', models.ForeignKey(to='planetofheroes.Campania')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
