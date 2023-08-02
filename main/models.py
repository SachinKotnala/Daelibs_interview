# models.py

from django.db import models

class Sensor(models.Model):
    sensor_name = models.CharField(max_length=45, null=False, blank=False)
    mon_avg_count = models.PositiveIntegerField(default=0)
    tue_avg_count = models.PositiveIntegerField(default=0)
    wed_avg_count = models.PositiveIntegerField(default=0)
    thu_avg_count = models.PositiveIntegerField(default=0)
    fri_avg_count = models.PositiveIntegerField(default=0)
    sat_avg_count = models.PositiveIntegerField(default=0)
    sun_avg_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.sensor_name
    
    def get_average_count_by_day_of_week(self, start_date, end_date):
        events = self.sensor_events.filter(event_datetime__range=[start_date, end_date])
        total_count = sum(event.count for event in events)
        if events.exists():
            return total_count // events.count()
        return 0

class SensorEvent(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_events')
    event_datetime = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"Sensor: {self.sensor.sensor_name}, Event Datetime: {self.event_datetime}"
