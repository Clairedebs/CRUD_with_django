from atexit import register
from django.contrib import admin

from students import models

# Register your models here.
admin.site.register(models.Student)