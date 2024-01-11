# Generated by Django 4.1.1 on 2023-10-23 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_basereport_options_hvreport_load'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('responsible_office', models.CharField(max_length=1000, null=True)),
                ('action_taken', models.CharField(max_length=1000, null=True)),
                ('days_outstanding', models.CharField(max_length=1000, null=True)),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='defect_records', to='reports.basereport')),
            ],
        ),
    ]
