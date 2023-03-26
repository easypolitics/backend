from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Bills
from .pagination import BillsPagination
from .serializers import BillsSerializer

EXCLUDE_BILLS = settings.EXCLUDE_BILLS
CONGRESS = settings.CONGRESS_VERSION


class BillsView(generics.ListAPIView):
    queryset = Bills.objects.exclude(bill_type__in=EXCLUDE_BILLS).filter(filtered_date__isnull=False,
                                                                           congress_version=CONGRESS).order_by(
        "-filtered_date")
    serializer_class = BillsSerializer
    permission_classes = (AllowAny,)
    pagination_class = BillsPagination

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super(BillsView, self).dispatch(request, *args, **kwargs)
