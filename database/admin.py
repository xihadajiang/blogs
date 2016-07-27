# -*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.contenttypes.models import content_type
from database.models import content_type
#from django.contrib.contenttypes.admin import ContenttypesAdmin

class DataAdmin(admin.ModelAdmin):
    search_fields = ('model',)
    list_filter = ('app_label', 'model')
    list_display = ('app_label', 'model')
    fields = ('app_label', 'model')

admin.site.register(content_type , DataAdmin)
