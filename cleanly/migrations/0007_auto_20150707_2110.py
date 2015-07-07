# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanly', '0005_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(null=True, upload_to=b'images/'),
        ),
    ]
