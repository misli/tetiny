# -*- coding: utf-8 -*-

"""
Django settings for tetiny project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

# Application definition
INSTALLED_APPS = [
    'tetiny',
] + INSTALLED_APPS
