from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    created_at_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    creator = filters.ModelChoiceFilter(queryset=User.objects.all(), field_name='creator__username')
    status = filters.ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
