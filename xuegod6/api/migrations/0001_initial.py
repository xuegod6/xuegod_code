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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('createtime', models.DateField(default=datetime.datetime(2018, 12, 8, 12, 34, 12, 154491), verbose_name='创建时间', max_length=30)),
            ],
            options={
                'verbose_name': '用户表',
            },
        ),
    ]
