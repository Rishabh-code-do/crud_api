import django_filters
from api.models import Box

class BoxFilterSet(django_filters.FilterSet):
    '''
        This Django FilterSet class, `BoxFilterSet`, is designed for the `Box` model.
        It includes filters for numeric fields such as length, breadth, height, area, and volume,
        as well as filters for the created_at (datetime) field and the related model's username field.
        The filters support both less than (`lt`) and greater than (`gt`) lookup expressions.
        This provides a convenient way to filter and query Box objects based on specified criteria.
    '''
    # Define filters for numeric fields
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
    # Define filters for datetime field
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    # Define filter for a related model field (username)
    username = django_filters.CharFilter(field_name='created_by__username')

    class Meta:
        model = Box
        # Define filter fields for the Box model
        fields = ['length__lt', 'length__gt', 'breadth__lt', 'breadth__gt', 'height__gt', 'height__lt',
                  'area__gt', 'area__lt', 'volume__gt', 'volume__lt', 'created_at__lt', 'created_at__gt', 'username']