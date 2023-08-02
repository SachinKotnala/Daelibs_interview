from django.urls import path
from .views import TrafficDayOfWeekAverageCount

urlpatterns = [
    path('dayOfWeekAverageCount', TrafficDayOfWeekAverageCount.as_view(), name='traffic-dayOfWeekAverageCount'),
]