# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auftrag',
            fields=[
                ('aid', models.AutoField(serialize=False, primary_key=True)),
                ('aupload', models.FileField(default=b'null', upload_to=b'docs/')),
            ],
        ),
        migrations.CreateModel(
            name='Dienstleistungsart',
            fields=[
                ('dname', models.CharField(max_length=30)),
                ('did', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('kname', models.CharField(max_length=30)),
                ('kid', models.AutoField(serialize=False, primary_key=True)),
                ('adresse', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rechnung',
            fields=[
                ('rid', models.AutoField(serialize=False, primary_key=True)),
                ('rnummer', models.CharField(max_length=30)),
                ('rdatum', models.DateField()),
                ('rupload', models.FileField(default=b'null', upload_to=b'docs/')),
            ],
        ),
        migrations.AddField(
            model_name='auftrag',
            name='did',
            field=models.ManyToManyField(to='manageme.Dienstleistungsart'),
        ),
        migrations.AddField(
            model_name='auftrag',
            name='kid',
            field=models.ForeignKey(to='manageme.Kunde'),
        ),
        migrations.AddField(
            model_name='auftrag',
            name='rid',
            field=models.ManyToManyField(to='manageme.Rechnung', blank=True),
        ),
    ]
