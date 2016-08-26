# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Monopoly', '0003_buyshares_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyshares',
            name='buyprice',
            field=models.DecimalField(null=True, verbose_name='\u8d2d\u4e70\u4ef7\u683c', max_digits=4, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='buytime',
            field=models.DateTimeField(null=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='cellprice',
            field=models.DecimalField(null=True, verbose_name='\u5356\u51fa\u4ef7\u683c', max_digits=4, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='numofshares',
            field=models.IntegerField(null=True, verbose_name='\u80a1\u6570'),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='reason',
            field=models.TextField(null=True, verbose_name='\u8d2d\u4e70\u7406\u7531'),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='selltime',
            field=models.DateTimeField(null=True, verbose_name='\u5356\u51fa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='sharescode',
            field=models.CharField(max_length=10, verbose_name='\u80a1\u7968\u4ee3\u7801'),
        ),
        migrations.AlterField(
            model_name='buyshares',
            name='sharesname',
            field=models.CharField(max_length=20, verbose_name='\u80a1\u7968\u540d'),
        ),
        migrations.AlterField(
            model_name='users',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 25, 13, 5, 21, 361882), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastip',
            field=models.IPAddressField(null=True, verbose_name='\u6700\u540e\u767b\u5f55IP'),
        ),
        migrations.AlterField(
            model_name='users',
            name='lasttime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='level',
            field=models.IntegerField(default=0, verbose_name='\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='users',
            name='passwd',
            field=models.CharField(max_length=200, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=30, verbose_name='\u5e10\u53f7\u540d'),
        ),
    ]
