# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('planetofheroes', '0006_auto_20141207_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='user',
            field=models.ForeignKey(related_name='rel_donacion', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='user',
            field=models.ForeignKey(related_name='volunter', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
