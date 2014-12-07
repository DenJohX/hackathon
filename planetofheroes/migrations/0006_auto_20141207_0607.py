# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('planetofheroes', '0005_voluntario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='user',
            field=models.OneToOneField(related_name='rel_donacion', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
