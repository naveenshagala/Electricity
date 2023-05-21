from rest_framework import generics
from .models import Metric
from .serializers import MetricSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

class MetricListCreateView(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def get_queryset(self):
        start_time = self.request.query_params.get('start')
        end_time = self.request.query_params.get('end')
        if start_time and end_time:
            return Metric.objects.filter(datetime__range=[start_time,end_time])
        else:
            return Metric.objects.all()
        

class MetricCreateView(generics.CreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
