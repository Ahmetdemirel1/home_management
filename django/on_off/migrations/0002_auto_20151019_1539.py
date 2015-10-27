# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on_off', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='signal',
            new_name='signal_on',
        ),
        migrations.AddField(
            model_name='device',
            name='signal_off',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
