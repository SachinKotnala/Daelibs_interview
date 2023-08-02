# Generated by Django 4.2.3 on 2023-07-28 13:29

from django.db import migrations, models
import django.db.models.deletion
import datetime
import time
import random
import pytz

def insert_random_data(apps, schema_editor):
    Sensor = apps.get_model("main", "Sensor")
    SensorEvent = apps.get_model("main", "SensorEvent")

    sensors = []
    for index in range(1,11):
        sensor = Sensor()
        sensor.name = index
        sensor.save()
        sensors.append(sensor)

    today = datetime.datetime.now()
    timedelta = datetime.timedelta(days=90)
    today_timestamp = int(time.mktime(today.timetuple()))
    last_year_from_today_timestamp = int(time.mktime((today-timedelta).timetuple()))
    count = 0
    for event_datetime in random.sample(range(last_year_from_today_timestamp, today_timestamp), 1000000):
        count +=1
        sensor_event = SensorEvent()
        sensor_event.sensor = sensors[random.randint(0,9)]
        sensor_event.event_datetime = datetime.datetime.fromtimestamp(event_datetime, tz=pytz.UTC)
        sensor_event.save()

def reverse_random_data(apps, schema_editor):
    Sensor = apps.get_model("main", "Sensor")
    Sensor.objects.all().delete()
    SensorEvent = apps.get_model("main", "SensorEvent")
    SensorEvent.objects.all().delete()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SensorEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_datetime', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sensor')),
            ],
        ),
        migrations.RunPython(insert_random_data, reverse_random_data),
    ]