from rest_framework import serializers

from base.serializers import FeederSerializer
from .models import *


# Create HV report object
class HVReportCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = HVReport
        fields = ['pk', 'report', 'feeder', 'outage_description', 'date_time_out', 'date_time_restored', 'hold_datetime_restored','hold_datetime_out','load', 'cause', 'remarks']


# List HV report objects together with feeder details
class HVReportListSerializer(serializers.ModelSerializer):

    # Use feeder serializer to display feeder details
    feeder = FeederSerializer()

    class Meta:
        model = HVReport
        fields = ['pk', 'report', 'feeder', 'outage_description','date_time_restored', 'date_time_out','load', 'cause', 'remarks']


# Defect Serializer
class DefectSerializer(serializers.ModelSerializer):

    class Meta:
        model = DefectReport
        fields = ['report', 'date_reported', 'description', 'responsible_office', 'action_taken', 'days_outstanding', 'remarks']


# Forced Outages

# Forced Outages list Serializer
class ForcedOutageListSerializer(serializers.ModelSerializer):

    feeder = FeederSerializer()

    class Meta:
        model = ForcedOutageReport
        fields = [
            'report', 'feeder', 'installed_capacity','pk', 'load',
            'number_of_tx', 'affected_areas', 'outage_description',
            'cause', 'remarks','date_time_out', 'date_time_restored',
        ]

# Forced Outages Create Serializer
class ForcedOutageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForcedOutageReport
        fields = [
            'report', 'feeder', 'installed_capacity', 'load',
            'number_of_tx', 'affected_areas', 'outage_description',
            'cause', 'remarks','hold_date_time_out', 'hold_date_time_retored','date_time_out', 'date_time_restored',
        ]


# Planned outage

# create
class PlannedOutageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlannedOutage
        fields = [
            'report', 'feeder', 'installed_capacity','pk', 'load',
            'number_of_tx', 'affected_areas', 'outage_description',
            'cause', 'remarks','planned_date_time_out', 'planned_date_time_restored','actual_date_time_out', 'actual_date_time_restored',
        ]

# List Serializer
class PlannedOutageListSerializer(serializers.ModelSerializer):

    feeder = FeederSerializer()

    class Meta:
        model = PlannedOutage
        fields = [
            'report', 'feeder', 'installed_capacity','pk', 'load',
            'number_of_tx', 'affected_areas', 'outage_description',
            'cause', 'remarks','planned_date_time_out', 'planned_date_time_restored','actual_date_time_out', 'actual_date_time_restored',
        ]



# List all SES reports with hv reports, load shedding reports, planned 
# outages, forced outages and defects reports associated with each report
class BaseReportListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='base-report-detail',
        lookup_field='pk'
    )

    # Use the HV report List serializer for HV reports list
    hv_report = HVReportListSerializer(many=True)

    # Use the Defects list for all report defects
    defect_records = DefectSerializer(many=True)

    # Use the Forced Outage list for all forced outages
    forced_outage_records = ForcedOutageListSerializer(many=True)

    # Use the Planned Outage list for all planned outages
    planned_outage_records = PlannedOutageListSerializer(many=True)

    class Meta:
        model= BaseReport
        fields = ['url', 'pk', 'name', 'date', 'hv_report', 'defect_records', 'forced_outage_records', 'planned_outage_records']


# serializer for creating the base report
class BaseReportCreateSerializer(serializers.ModelSerializer):

    # url = serializers.HyperlinkedIdentityField(
    #     view_name='feeder-single',
    #     lookup_field='pk'
    # )

    class Meta:
        model= BaseReport
        fields = ['pk', 'name', 'date', 'created']

