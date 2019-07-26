# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('publishTime', models.DateTimeField()),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('createTime', models.DateTimeField()),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
