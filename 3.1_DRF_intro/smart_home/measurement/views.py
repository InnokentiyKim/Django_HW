# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class ListCreateAPIView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        return Response(SensorSerializer(sensors, many=True).data)

    def post(self, request):
        sensor_deserializer = SensorSerializer(data=request.data, many=False)
        if sensor_deserializer.is_valid():
            Sensor.objects.create(**sensor_deserializer.validated_data)
        return Response({'Status': 'Successfully created'}, status=201)


class RetrieveUpdateAPIView(APIView):
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        sensor.description = request.data.get('description')
        sensor.save()
        return Response({'Status': 'Successfully updated'}, status=200)


class CreateAPIView(APIView):
    def post(self, request):
        measurement = MeasurementSerializer(data=request.data, many=False)
        if measurement.is_valid():
            sensor = Sensor.objects.get(pk=measurement.validated_data.get('sensor'))
            temperature = measurement.validated_data.get('temperature')
            measurement_obj = Measurement.objects.create(sensor=sensor, temperature=temperature)
            return Response({'Status': 'Successfully created', 'id': measurement_obj.id}, status=201)
        return Response(measurement.errors, status=400)
