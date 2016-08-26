# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Monopoly', '0002_auto_20160820_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyshares',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=django.db.models.fields.IntegerField, primary_key=True)),
                ('buytime', models.DateTimeField(null=True)),
                ('selltime', models.DateTimeField(null=True)),
                ('sharesname', models.CharField(max_length=20)),
                ('sharescode', models.CharField(max_length=10)),
                ('reason', models.TextField(null=True)),
                ('buyprice', models.DecimalField(null=True, max_digits=4, decimal_places=3)),
                ('cellprice', models.DecimalField(null=True, max_digits=4, decimal_places=3)),
                ('numofshares', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=django.db.models.fields.IntegerField, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=200)),
                ('level', models.IntegerField(default=0)),
                ('createtime', models.DateTimeField(null=True)),
                ('lasttime', models.DateTimeField(null=True)),
                ('lastip', models.IPAddressField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
