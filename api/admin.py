from django.contrib import admin
import api.models

admin.site.register(api.models.Item)
admin.site.register(api.models.Version)
