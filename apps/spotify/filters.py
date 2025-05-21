import django_filters
from .models import Author

class AuthorFilter(django_filters.FilterSet):
    min_albums = django_filters.NumberFilter(field_name='album_count', lookup_expr='gte')
    max_albums = django_filters.NumberFilter(field_name='album_count', lookup_expr='lte')

    class Meta:
        model = Author
        fields = ['min_albums', 'max_albums']