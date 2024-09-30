from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        sensor = Sensor.objects.create(**serializer.validated_data)
        return Response(SensorSerializer(sensor).data, status=201)


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = self.queryset.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        sensor.description = request.data['description']
        sensor.save()
        return Response(SensorSerializer(sensor).data, status=200)


class CreateAPIView(APIView):
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_measurement = Measurement.objects.create(**serializer.validated_data)
        return Response(MeasurementSerializer(new_measurement).data, status=201)
