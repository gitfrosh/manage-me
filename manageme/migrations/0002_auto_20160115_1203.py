# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auftrag',
            name='aupload',
            field=models.FileField(default=b'sample.txt', upload_to=b'docs/'),
        ),
    ]
