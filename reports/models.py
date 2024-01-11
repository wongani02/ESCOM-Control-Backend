from django.db import models
from base.models import Feeder

# Create your models here.


class BaseReport(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    

class HVReport(models.Model):
    report = models.ForeignKey(BaseReport, on_delete=models.CASCADE, related_name='hv_report')
    feeder = models.ForeignKey(Feeder, on_delete=models.DO_NOTHING, related_name='hv_report_feeder')
    outage_description = models.CharField(max_length=1000)
    date_time_out = models.CharField(null=True, max_length=1000)
    date_time_restored = models.CharField(null=True, max_length=1000)
    load = models.PositiveIntegerField(null=True)
    duration = models.CharField(max_length=100)
    cause = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)
    hold_datetime_restored = models.DateTimeField(null=True)
    hold_datetime_out = models.DateTimeField(null=True)

    def __str__(self):
        return self.outage_description

    # def save(self, *arg, **kwargs):
    #     pass

class PlannedOutage(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.CASCADE, null=True)
    report = report = models.ForeignKey(BaseReport, on_delete=models.CASCADE, related_name='planned_outage_records', null=True)
    cause = models.CharField(max_length=1000, null=True)
    remarks= models.CharField(max_length=1000, null=True)
    installed_capacity = models.PositiveIntegerField(null=True)
    number_of_tx = models.PositiveIntegerField(null=True)
    affected_areas= models.CharField(max_length=1000, null=True)
    outage_description = models.CharField(max_length=1000, null=True)
    planned_date_time_out= models.CharField(max_length=1000, null=True)
    planned_date_time_restored = models.CharField(max_length=1000, null=True)
    actual_date_time_out = models.CharField(max_length=1000, null=True)
    actual_date_time_restored = models.CharField(max_length=1000, null=True)
    load=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.outage_description



class ForcedOutageReport(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.CASCADE, null=True)
    report = report = models.ForeignKey(BaseReport, on_delete=models.CASCADE, related_name='forced_outage_records', null=True)
    cause = models.CharField(max_length=1000, null=True)
    remarks= models.CharField(max_length=1000, null=True)
    installed_capacity = models.PositiveIntegerField(null=True)
    number_of_tx = models.PositiveIntegerField(null=True)
    affected_areas= models.CharField(max_length=1000, null=True)
    outage_description= models.CharField(max_length=1000, null=True)
    hold_date_time_out = models.CharField(max_length=1000, null=True)
    hold_date_time_retored = models.CharField(max_length=1000, null=True)
    date_time_out = models.DateTimeField(null=True)
    date_time_restored = models.DateTimeField(null=True)
    load = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.cause

class LoadSheddingReport(models.Model):
    pass


class DefectReport(models.Model):
    report = models.ForeignKey(BaseReport, on_delete=models.CASCADE, related_name='defect_records', null=True)
    date_reported = models.DateField(null=True)
    description = models.CharField(max_length=1000, null=True)
    responsible_office = models.CharField(max_length=1000, null=True)
    action_taken = models.CharField(max_length=1000, null=True)
    days_outstanding = models.CharField(max_length=1000, null=True)
    remarks = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.description
