# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monopoly', '0004_auto_20160825_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyshares',
            name='buyprice',
            field=models.DecimalField(null=True, verbose_name='\u8d2d\u4e70\u4ef7\u683c', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='cellprice',
            field=models.DecimalField(null=True, verbose_name='\u5356\u51fa\u4ef7\u683c', max_digits=10, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='reason',
            field=models.TextField(null=True, verbose_name='\u8d2d\u4e70\u7406\u7531', blank=True),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='selltime',
            field=models.DateTimeField(null=True, verbose_name='\u5356\u51fa\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='sharescode',
            field=models.CharField(max_length=10, verbose_name='\u80a1\u7968\u4ee3\u7801', blank=True),
        ),
    ]
