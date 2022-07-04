from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import funds1, funds2, funds3, funds4, funds5, funds6, funds7, funds8

class funds1Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds1, funds1Admin)

class funds2Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds2, funds2Admin)

class funds3Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds3, funds3Admin)

class funds4Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds4, funds4Admin)

class funds5Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds5, funds5Admin)

class funds6Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds6, funds6Admin)

class funds7Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds7, funds7Admin)

class funds8Admin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(funds8, funds8Admin)
