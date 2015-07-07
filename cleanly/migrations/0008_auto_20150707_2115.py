# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanly', '0007_auto_20150707_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='product_decription',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]
