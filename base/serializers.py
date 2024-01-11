from rest_framework import serializers

from .models import *


class FeederSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='feeder-single',
        lookup_field='pk'
    )

    class Meta:
        model = Feeder
        fields = ['url', 'pk', 'feeder', 'number_of_transformers', 'areas', 'domestic', 'commercial', 'industrial', 'installed_capacity']


class SubstationSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ss-single', 
        lookup_field='pk',
    )

    feeder_lines = FeederSerializer(many=True)

    class Meta:
        model = Substation
        fields = ['url', 'name', 'electrical_district', 'ssrating', 'installed_cap', 'number_of_feeders', 'feeder_lines']


class LoadSheddingSerializer(serializers.ModelSerializer):

    feeders = FeederSerializer(many=True)

    class Meta:
        model = LoadSheddingGroup
        fields = ['group_name', 'feeders']


class MimicNumberSerializer(serializers.ModelSerializer):

    # feeder = FeederSerializer()

    class Meta:
        model = MimicNumber
        fields = ['pk', 'feeder', 'mimic_number', 'date', 'size', 'description', 'location',]


class TXRecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TXReplacementRecord
        fields = ['pk', 'feeder', 'location', 'date', 'substation_number', 'capacity', 'year', 'serial_number', 'manufacturer', 'remarks']
        

