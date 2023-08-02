"""
  This file provides the serializer(s) for Senser model

"""
from rest_framework import serializers
from .models import Sensor

class AverageDOWTrafficCountSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'mon_avg_count', 'tue_avg_count', 'wed_avg_count', 'thu_avg_count', 'fri_avg_count', 'sat_avg_count', 'sun_avg_count']