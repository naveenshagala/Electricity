from django.urls import path
from .views import MetricListCreateView, MetricCreateView

urlpatterns = [
    path('', MetricListCreateView.as_view(), name='get_metrics'),
    path('create/', MetricCreateView.as_view(), name='create_metric'),
]