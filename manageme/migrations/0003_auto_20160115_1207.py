# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageme', '0002_auto_20160115_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auftrag',
            name='aupload',
            field=models.FileField(default=b'docs/sample.txt', upload_to=b'docs/'),
        ),
    ]
