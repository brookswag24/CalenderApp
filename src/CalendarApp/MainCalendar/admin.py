from django.contrib import admin

# Register your models here.

from .models import SaintDay
from .models import FastDays

admin.site.register(SaintDay)
admin.site.register(FastDays)
