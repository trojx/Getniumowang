# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monopoly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatcontent',
            name='sharesname',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
