from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from .permissions import IsOwnerOrIsAdmin
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        """Фильтрация запросов"""
        queryset = Advertisement.objects.filter(status__in=["OPEN", "CLOSED"])
        creator = self.request.user
        if creator and creator in User.objects.all():
            add_queryset = Advertisement.objects.filter(status="DRAFT").filter(creator=creator)
            print("add_queryset is ", add_queryset)
            queryset = queryset | add_queryset
        return queryset


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrIsAdmin(), ]
        elif self.action in ["create", ]:
            return [IsAuthenticated(), ]
        elif self.action in ["retrieve", "list"]:
            return [IsOwnerOrReadOnly(), ]
        return [IsAdminUser(), ]
