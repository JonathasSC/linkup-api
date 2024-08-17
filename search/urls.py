from django.urls import path
from .viewsets import SearchAPIView

urlpatterns = [
    path('', SearchAPIView.as_view(), name='search'),
]
