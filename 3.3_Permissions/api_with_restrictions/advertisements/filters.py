from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at", label="created_at")
    creator = filters.ModelChoiceFilter(queryset=User.objects.all(), field_name="creator", label="creator")
    status = filters.ChoiceFilter(field_name="status", choices=AdvertisementStatusChoices.choices, label="status")


    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
