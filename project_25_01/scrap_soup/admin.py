from django.contrib import admin
from .models import AuthorName, QuoteName


@admin.register(AuthorName)
class AuthorNameAdmin(admin.ModelAdmin):
    list_display = ("name", "time")
    list_filter = ("time", "name")
    search_fields = ("time", "name")

@admin.register(QuoteName)
class QuoteNameAdmin(admin.ModelAdmin):
    pass