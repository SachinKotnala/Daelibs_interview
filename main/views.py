# views.py

import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sensor, SensorEvent  
from .serializers import AverageDOWTrafficCountSerializer

class TrafficDayOfWeekAverageCount(APIView):
    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Fetch all SensorEvent instances within the specified date range
        events = SensorEvent.objects.filter(event_datetime__range=[start_date, end_date])

         # Create a dictionary to store the total count and count for each day of the week for each sensor
        sensor_day_count = {}

        # Calculate the total count and count for each day of the week for each sensor
        # Just a thought: Maybe this could be done in SQL to improve efficiency 
        for event in events:
            day_of_week = event.event_datetime.weekday()  # Get the day of the week as an integer
            sensor_id = event.sensor.id
            if sensor_id not in sensor_day_count:
                sensor_day_count[sensor_id] = {
                    0: 0,  # Monday
                    1: 0,  # Tuesday
                    2: 0,  # Wednesday
                    3: 0,  # Thursday
                    4: 0,  # Friday
                    5: 0,  # Saturday
                    6: 0,  # Sunday
                }
            sensor_day_count[sensor_id][day_of_week] += 1
       # list of dictionaries containing average counts for each sensor
        data = []
        for sensor_id, day_count in sensor_day_count.items():
            sensor = Sensor.objects.get(pk=sensor_id)
            avg_data = {
                'sensor_id': sensor_id,
                'sensor_name': str(sensor.id),
                'mon_avg_count': day_count[0],
                'tue_avg_count': day_count[1],
                'wed_avg_count': day_count[2],
                'thu_avg_count': day_count[3],
                'fri_avg_count': day_count[4],
                'sat_avg_count': day_count[5],
                'sun_avg_count': day_count[6],
            }
            data.append(avg_data)

        serializer = AverageDOWTrafficCountSerializer(data, many=True)
        return Response({'results': serializer.data})
