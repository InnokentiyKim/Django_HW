from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        required_fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'measured_at']
        write_only_fields = ['sensor', 'temperature']
        required_fields = ['sensor', 'temperature']



class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        required_fields = ['name', 'description']

