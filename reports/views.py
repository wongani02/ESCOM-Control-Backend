from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *
# Create your views here.


# Report Serializers
class BaseReportListAPIView(generics.ListAPIView):
    serializer_class = BaseReportListSerializer
    permission_classes = [AllowAny]
    queryset = BaseReport.objects.all()


class BaseReportCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BaseReportCreateSerializer
    permission_classes = [AllowAny]
    queryset = BaseReport.objects.all()


class BaseReportDetailView(generics.RetrieveAPIView):
    serializer_class = BaseReportListSerializer
    permission_classes = [AllowAny]
    queryset = BaseReport.objects.all()


#HV reports serializers
class HVReportListAPIView(generics.ListAPIView):
    serializer_class = HVReportListSerializer
    permission_classes = [AllowAny]
    queryset = HVReport.objects.all()


class HVReportCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HVReportCreateSerializer
    permission_classes = [AllowAny]
    queryset = HVReport.objects.all()

    def perform_create(self, serializer):
        date_time_out= serializer.validated_data.get('date_time_out')
        date_time_restored = serializer.validated_data.get('date_time_restored') 

        date_time_restored_hold = serializer.validated_data.get('hold_datetime_restored') or None
        date_time_out_hold = serializer.validated_data.get('hold_datetime_out') or None

        date_format = '%Y-%m-%dT%H:%M'

        if date_time_restored_hold is None:
            date_time_restored_hold = datetime.strptime(date_time_restored, date_format)

        if date_time_out_hold is None:
            date_time_out_hold = datetime.strptime(date_time_out, date_format)
        
        serializer.save(hold_datetime_out=date_time_out_hold,hold_datetime_restored=date_time_restored_hold)


# Defect Serializer
class DefectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DefectSerializer
    permission_classes = [AllowAny]
    queryset = DefectReport.objects.all()


# Forced Outages
class ForcedOutageListCreateView(generics.ListCreateAPIView):
    serializer_class = ForcedOutageCreateSerializer
    permission_classes = [AllowAny]
    queryset = ForcedOutageReport.objects.all()

    def perform_create(self, serializer):
        hold_time_out = serializer.validated_data.get('hold_date_time_out')
        hold_time_restored = serializer.validated_data.get('hold_date_time_retored') 

        actual_time_out = serializer.validated_data.get('date_time_out') or None
        actual_time_restored = serializer.validated_data.get('date_time_restored')

        date_format = '%Y-%m-%dT%H:%M'

        if actual_time_restored is None:
            actual_time_restored = datetime.strptime(hold_time_restored, date_format)

        if actual_time_out is None:
            actual_time_out = datetime.strptime(hold_time_out, date_format)

        serializer.save(date_time_out=actual_time_out, date_time_restored=actual_time_restored)


class PlannedOutageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PlannedOutageCreateSerializer
    permission_classes = [AllowAny]
    queryset = PlannedOutage.objects.all()
