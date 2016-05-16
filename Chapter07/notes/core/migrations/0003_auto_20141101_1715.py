# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_note_docfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='docfile',
            new_name='attach',
        ),
    ]
