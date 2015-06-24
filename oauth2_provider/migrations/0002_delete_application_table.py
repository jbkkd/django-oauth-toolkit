# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from oauth2_provider.settings import oauth2_settings
from django.db import models, migrations
import oauth2_provider.validators
import oauth2_provider.generators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0001_initial')
    ]

    operations = [
        migrations.DeleteModel(
            'application'
        )
    ]
