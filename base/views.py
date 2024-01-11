from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *

# Create your views here.


class SubstationsAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer


class SubstationsingleAPIView(generics.RetrieveAPIView):
    serializer_class = SubstationSerializer
    permission_classes = [AllowAny]
    queryset = Substation.objects.all()


class FeederSingleAPIView(generics.RetrieveAPIView):
    serializer_class = FeederSerializer
    permission_classes = [AllowAny]
    queryset = Feeder.objects.all()


class FeedersAPIView(generics.ListAPIView):
    serializer_class = FeederSerializer
    permission_classes = [AllowAny]
    queryset = Feeder.objects.all()


class LoadSheddingAPIView(generics.ListAPIView):
    serializer_class = LoadSheddingSerializer
    permission_classes = [AllowAny]
    queryset = LoadSheddingGroup.objects.all()


class MimicNumberListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MimicNumberSerializer
    permission_classes = [AllowAny]
    queryset = MimicNumber.objects.all()


class TXRecordSerializerListCreateView(generics.ListCreateAPIView):
    serializer_class = TXRecordsSerializer
    permission_classes = [AllowAny]
    queryset = TXReplacementRecord.objects.all()

