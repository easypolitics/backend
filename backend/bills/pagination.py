from rest_framework import pagination


class BillsPagination(pagination.PageNumberPagination):
    page_size = 20
