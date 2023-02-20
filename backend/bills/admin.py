from django.contrib import admin

from .models import Bills


class BillsAdmin(admin.ModelAdmin):
    list_display = ("bill_id", "short_title")


admin.site.register(Bills, BillsAdmin)
