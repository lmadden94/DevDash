from django.contrib import admin

from .models import Project, Enhancement, Bug

# Register your models here.

admin.site.register(Project)
admin.site.register(Enhancement)
admin.site.register(Bug)