from django.contrib.auth.models import User
from rest_framework import serializers
from api_with_restrictions.settings import OPEN_ADV_LIMIT
from advertisements.models import AdvertisementStatusChoices
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', )


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        print(data.get("status"))
        print(data.get("title"))
        # TODO: добавьте требуемую валидацию
        if (data.get("status", "OPEN") == AdvertisementStatusChoices.OPEN and
                Advertisement.objects.filter(status=AdvertisementStatusChoices.OPEN).count() >= OPEN_ADV_LIMIT):
            raise serializers.ValidationError(f"Can't create more than {OPEN_ADV_LIMIT} open advertisements")

        return data
