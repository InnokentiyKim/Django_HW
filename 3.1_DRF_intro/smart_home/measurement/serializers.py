from rest_framework import serializers

from measurement.models import Sensor


# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()


class MeasurementSerializer(serializers.Serializer):
    sensor = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    temperature = serializers.FloatField()
    measured_at = serializers.DateTimeField(read_only=True, required=False)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = '__all__'

