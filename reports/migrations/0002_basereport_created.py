# Generated by Django 4.1.1 on 2023-09-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basereport',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
