from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from .models import Metric
from .serializers import MetricSerializer

class MetricAPITestCase(APITestCase):

    def setUp(self):
        Metric.objects.create(datetime=datetime(2023, 1, 1, 12, 0, 0), voltage=220, current=5)
        Metric.objects.create(datetime=datetime(2023, 1, 2, 12, 0, 0), voltage=230, current=7)

    def test_get_metrics(self):
        url = reverse('get_metrics')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_filtered_metrics(self):
        url = reverse('get_metrics')
        start_time = '2023-01-01T00:00:00'
        end_time = '2023-01-02T23:59:59'
        response = self.client.get(url, {'start': start_time, 'end': end_time})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_create_metric(self):
       
        url = reverse('create_metric')
        data = {'datetime': '2023-01-03T12:00:00', 'voltage': 240, 'current': 6}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Metric.objects.count(), 3)  

      
        metric = Metric.objects.get(datetime=datetime(2023, 1, 3, 12, 0, 0))
        serializer = MetricSerializer(metric)
        self.assertEqual(response.data, serializer.data)
