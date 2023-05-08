from django.contrib import admin
from .models import HashInfoModel, ImplantInfoModel


@admin.register(HashInfoModel)
class HashInfoModelAdmin(admin.ModelAdmin):
    list_display = ("hash_name", "when_used")
    list_filter = ("edition_year",)
    search_fields = ("when_used__startswith", )

@admin.register(ImplantInfoModel)
class ImplantInfoModelAdmin(admin.ModelAdmin):
    list_display = ("implant_name", "strange_type")
    list_filter = ("defense",)
    search_fields = ("implant_name__startswith", )