from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("backend.bills.urls", namespace="bills")),
    path("", lambda req: redirect("v1/bills"))
]

admin.site.site_header = getattr(settings, "ADMIN_SITE_HEADER")
admin.site.index_title = getattr(settings, "ADMIN_SITE_INDEX_TITLE")
admin.site.site_title = getattr(settings, "ADMIN_SITE_TITLE")


def page_not_found(request, exception):
    response = {
        "detail": "Not found."
    }

    return JsonResponse(response, status=404)


def server_error(request):
    response = {
        "detail": "The server encountered an internal error."
    }

    return JsonResponse(response, status=500)


handler404 = page_not_found
handler500 = server_error
