from __future__ import unicode_literals

from django.contrib import admin
from .models import client,Product


admin.site.register(client)
admin.site.register(Product)