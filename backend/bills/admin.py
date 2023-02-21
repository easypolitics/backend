from django.contrib import admin

from .models import Bills


class BillsAdmin(admin.ModelAdmin):
    list_display = ("bill_id", "short_title")
    search_fields = ["bill_id", "summary"]


admin.site.register(Bills, BillsAdmin)
