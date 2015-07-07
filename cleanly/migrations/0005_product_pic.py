# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanly', '0004_auto_20150707_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.ImageField(default=None, upload_to=b'images/'),
        ),
    ]
