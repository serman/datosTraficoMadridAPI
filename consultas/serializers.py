from rest_framework import serializers

class BasicQuerySerializer(serializers.Serializer):
    point = serializers.IntegerField(read_only=True)
    day = serializers.IntegerField(read_only=True)
    month = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField(read_only=True)
#El medidor 4418 el día 4 del mes 10 del año 2017 a las 0 horas y 0 minutos tuvo unas mediciones de 389 intensidad, 1 ocupación, 22 carga y 0 velocidad media


class MedidorData(object):
    def __init__(self, id, day, month, year, hour, minute, intensity, occupancy, load, avgspeed):
        self.id = id
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.intensity = intensity
        self.occupancy = occupancy
        self.load = load
        self.avgspeed = avgspeed


class MedidorDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    day = serializers.IntegerField(read_only=True)
    month = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    hour = serializers.IntegerField(read_only=True)
    minute = serializers.IntegerField(read_only=True)

    intensity = serializers.IntegerField(read_only=True)
    occupancy = serializers.IntegerField(read_only=True)
    load = serializers.IntegerField(read_only=True)
    avgspeed = serializers.IntegerField(read_only=True)
