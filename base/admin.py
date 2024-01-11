from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *

# Register your models here.


class FeederInline(admin.StackedInline):
    model = Feeder
    extra = 0


@admin.register(Substation)
class SubstationModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'ssrating']
    search_fields = ['name']
    inlines = [FeederInline]


admin.site.register(Feeder, ImportExportModelAdmin)

admin.site.register(LoadSheddingGroup, ImportExportModelAdmin)

admin.site.register(TXReplacementRecord, ImportExportModelAdmin)