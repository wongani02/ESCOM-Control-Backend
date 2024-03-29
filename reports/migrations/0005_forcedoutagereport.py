# Generated by Django 4.1.1 on 2023-10-23 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_mimicnumber_mimic_number'),
        ('reports', '0004_defectreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForcedOutageReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=1000)),
                ('remarks', models.CharField(max_length=1000)),
                ('installed_capacity', models.PositiveIntegerField(null=True)),
                ('number_of_tx', models.PositiveIntegerField(null=True)),
                ('affected_areas', models.CharField(max_length=1000)),
                ('outage_description', models.CharField(max_length=1000)),
                ('hold_date_time_out', models.CharField(max_length=1000)),
                ('date_time_out', models.DateTimeField(null=True)),
                ('date_time_restored', models.DateTimeField(null=True)),
                ('load', models.PositiveIntegerField(null=True)),
                ('feeder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.feeder')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forced_outage_records', to='reports.basereport')),
            ],
        ),
    ]
