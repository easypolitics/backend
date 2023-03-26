from django.contrib import admin

from .models import Bills


class BillsAdmin(admin.ModelAdmin):
    list_display = ("bill_id", "short_title", "introduced_date", "latest_major_action_date", "filtered_date")
    search_fields = ["bill_id", "summary"]


admin.site.register(Bills, BillsAdmin)
