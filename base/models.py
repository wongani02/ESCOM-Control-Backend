from django.db import models

# Create your models here.


class Substation(models.Model):
    name = models.CharField(max_length=500, null=True)
    electrical_district = models.CharField(max_length=500, null=True)
    ssrating = models.CharField(max_length=20, null=True)
    installed_cap= models.PositiveBigIntegerField(default=1, null=True)
    number_of_feeders = models.PositiveSmallIntegerField(default=1, null=True)

    def __str__(self):
        return self.name


class Feeder(models.Model):
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE, null=True, related_name='feeder_lines')
    feeder = models.CharField(max_length=500, null=True)
    number_of_transformers = models.PositiveSmallIntegerField(null=True)
    areas = models.CharField(max_length=10000, null=True)
    domestic = models.BooleanField(null=True, default=False)
    commercial = models.BooleanField(null=True, default=False)
    industrial = models.BooleanField(null=True, default=False)
    installed_capacity = models.PositiveBigIntegerField(default=1, null=True)

    def __str__(self):
        return f'{self.substation.name} - {self.feeder}'
    

class LoadSheddingGroup(models.Model):
    group_name = models.CharField(max_length=100, null=True)
    feeders = models.ManyToManyField(Feeder, related_name='loadshedding_feeders')

    def __str__(self):
        return self.group_name
    

class MimicNumber(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.CASCADE, null=True)
    mimic_number = models.CharField(max_length=1000, null=True)
    date = models.DateField(null=True)
    size = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=10000, null=True)
    location = models.CharField(null=True, max_length=1000)
    
    def __str__(self):
        return self.mimic_number

class TXReplacementRecord(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=1000, null=True)
    date = models.DateField(null=True)
    substation_number = models.PositiveIntegerField(null=True)
    capacity = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)
    serial_number = models.CharField(max_length=1000, null=True)
    manufacturer = models.CharField(max_length=1000, null=True)
    remarks = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.serial_number

