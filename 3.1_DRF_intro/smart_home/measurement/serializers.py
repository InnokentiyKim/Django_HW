from rest_framework import serializers

# TODO: опишите необходимые сериализаторы 
class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()


class MeasurementSerializer(serializers.Serializer):
    sensor = serializers.IntegerField()
    temperature = serializers.FloatField()

