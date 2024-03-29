# Generated by Django 4.1.1 on 2023-10-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_plannedoutage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hvreport',
            name='date_out',
        ),
        migrations.RemoveField(
            model_name='hvreport',
            name='date_restored',
        ),
        migrations.RemoveField(
            model_name='hvreport',
            name='time_out',
        ),
        migrations.RemoveField(
            model_name='hvreport',
            name='time_restored',
        ),
        migrations.AddField(
            model_name='hvreport',
            name='date_time_out',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='hvreport',
            name='date_time_restored',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='hvreport',
            name='hold_datetime_out',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hvreport',
            name='hold_datetime_retored',
            field=models.DateTimeField(null=True),
        ),
    ]
