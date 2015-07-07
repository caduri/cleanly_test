# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanly', '0002_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='artist',
            new_name='user',
        ),
    ]
