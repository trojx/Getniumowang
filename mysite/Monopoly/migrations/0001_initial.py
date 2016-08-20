# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatcontent',
            fields=[
                ('sharesname', models.CharField(max_length=16)),
                ('time', models.DateTimeField(null=True)),
                ('id', models.AutoField(serialize=False, verbose_name=django.db.models.fields.IntegerField, primary_key=True)),
                ('datapid', models.IntegerField(null=True)),
                ('chattxt', models.TextField()),
            ],
        ),
    ]
