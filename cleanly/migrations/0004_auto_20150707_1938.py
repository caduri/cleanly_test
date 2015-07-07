# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanly', '0003_auto_20150707_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
