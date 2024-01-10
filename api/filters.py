import django_filters
from api.models import Box

class BoxFilterSet(django_filters.FilterSet):
    length__lt = django_filters.NumberFilter(field_name='length', lookup_expr='lt')
    length__gt = django_filters.NumberFilter(field_name='length', lookup_expr='gt')
    breadth__lt = django_filters.NumberFilter(field_name='breadth', lookup_expr='lt')
    breadth__gt = django_filters.NumberFilter(field_name='breadth', lookup_expr='gt')
    height__gt = django_filters.NumberFilter(field_name='height', lookup_expr='gt')
    height__lt = django_filters.NumberFilter(field_name='height', lookup_expr='lt')
    area__gt = django_filters.NumberFilter(field_name='area', lookup_expr='gt')
    area__lt = django_filters.NumberFilter(field_name='area', lookup_expr='lt')
    volume__gt = django_filters.NumberFilter(field_name='volume', lookup_expr='gt')
    volume__lt = django_filters.NumberFilter(field_name='volume', lookup_expr='lt')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    username = django_filters.CharFilter(field_name='created_by__username')

    class Meta:
        model = Box
        fields = ['length__lt', 'length__gt', 'breadth__lt', 'breadth__gt', 'height__gt', 'height__lt',
                  'area__gt', 'area__lt', 'volume__gt', 'volume__lt', 'created_at__lt', 'created_at__gt', 'username']
