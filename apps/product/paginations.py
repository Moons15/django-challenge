from rest_framework.pagination import PageNumberPagination

__author__ = 'richard'


class SixPagination(PageNumberPagination):
    page_size = 6


class TenPagination(PageNumberPagination):
    page_size = 10


class TwentyPagination(PageNumberPagination):
    page_size = 20
