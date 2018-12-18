# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('createtime', models.DateTimeField(verbose_name='创建时间', default=datetime.datetime(2018, 12, 8, 20, 57, 51, 387214))),
            ],
            options={
                'verbose_name': '用户表',
            },
        ),
    ]
