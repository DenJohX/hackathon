# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planetofheroes', '0003_comentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('comentario', models.TextField(blank=True)),
                ('recompensa', models.IntegerField(null=True, blank=True)),
                ('campania', models.ForeignKey(to='planetofheroes.Campania')),
                ('user', models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
