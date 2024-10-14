from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from advertisements.models import Advertisement, Favourite
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
        """Получение списка объявлений"""
        queryset = Advertisement.objects.filter(status__in=["OPEN", "CLOSED"])
        creator = self.request.user
        if creator and creator in User.objects.all():
            add_queryset = Advertisement.objects.filter(status="DRAFT").filter(creator=creator)
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


    @action(permission_classes=[IsAuthenticated], detail=False, url_path=r"favourites")
    def favourites(self, request):
        """Получение списка избранных объявлений."""
        user = request.user
        queryset = Advertisement.objects.filter(favourites__user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['post', 'delete'], permission_classes=[IsAuthenticated], url_path=r'favourite')
    def favourite(self, request, pk=None):
        """Добавление или удаление объявления из избранного."""
        user = request.user
        advertisement = self.get_object()

        if not advertisement:
            return Response(status=400, data="Advertisement not found")
        if user == advertisement.creator:
            return Response(status=400, data="Can't add (delete) your own advertisement to (from) favourites")

        if request.method == 'POST':
            if Favourite.objects.filter(user=user, advertisement=advertisement).exists():
                return Response(status=400, data="Already in favourites")
            Favourite.objects.create(user=user, advertisement=advertisement)
            return Response(status=201, data="Added to favourites")

        if request.method == 'DELETE':
            favourite = Favourite.objects.filter(user=user, advertisement=advertisement)
            if not favourite.exists():
                return Response(status=400, data="Advertisement not found in favourites")
            favourite.delete()
            return Response(status=204, data="Removed from favourites")

