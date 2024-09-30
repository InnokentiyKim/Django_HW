from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='measurements/images/')
