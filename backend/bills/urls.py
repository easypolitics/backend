from django.urls import path

from .views import BillsView

app_name = "bills"

urlpatterns = [
    path("bills/", BillsView.as_view()),
]
