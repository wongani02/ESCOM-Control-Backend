# Generated by Django 4.1.1 on 2023-10-23 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_remove_hvreport_date_out_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hvreport',
            old_name='hold_datetime_retored',
            new_name='hold_datetime_restored',
        ),
    ]
