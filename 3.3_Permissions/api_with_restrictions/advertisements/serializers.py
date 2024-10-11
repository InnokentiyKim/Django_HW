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
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if data.get("status", "OPEN") == "OPEN":
            open_adv_count = (
                Advertisement.objects
                .filter(creator=self.context["request"].user)
                .filter(status=AdvertisementStatusChoices.OPEN)
                .count()
            )
            if open_adv_count >= OPEN_ADV_LIMIT:
                raise serializers.ValidationError(f"Can't create more than {OPEN_ADV_LIMIT} open advertisements")
        return data
