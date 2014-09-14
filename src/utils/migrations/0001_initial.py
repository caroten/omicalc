# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CirculationLimit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('limit', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Ограничения тиража',
                'ordering': ['limit'],
                'verbose_name': 'Ограничение тиража',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InkFaceBack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('face', models.IntegerField()),
                ('back', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Красочность',
                'ordering': ['face', 'back'],
                'verbose_name': 'Красочность',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrintFormat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название', max_length=16)),
                ('denominator', models.IntegerField(verbose_name='Знаменатель', help_text='Знаменатель для получения количества полос из условного А1')),
            ],
            options={
                'verbose_name_plural': 'Форматы печати',
                'ordering': ['denominator'],
                'verbose_name': 'Формат печати',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WasteRatio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Норматив')),
                ('ink', models.ForeignKey(to='utils.InkFaceBack')),
                ('limit', models.ForeignKey(to='utils.CirculationLimit')),
            ],
            options={
                'verbose_name_plural': 'Нормы отходов',
                'verbose_name': 'Норма отходов',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inkfaceback',
            name='values',
            field=models.ManyToManyField(to='utils.CirculationLimit', through='utils.WasteRatio'),
            preserve_default=True,
        ),
    ]
