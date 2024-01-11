# Generated by Django 4.1.1 on 2023-08-30 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeder', models.CharField(max_length=500, null=True)),
                ('number_of_transformers', models.PositiveSmallIntegerField(null=True)),
                ('areas', models.CharField(max_length=10000, null=True)),
                ('domestic', models.BooleanField(default=False, null=True)),
                ('commercial', models.BooleanField(default=False, null=True)),
                ('industrial', models.BooleanField(default=False, null=True)),
                ('installed_capacity', models.PositiveBigIntegerField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Substation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('electrical_district', models.CharField(max_length=500, null=True)),
                ('ssrating', models.CharField(max_length=20, null=True)),
                ('installed_cap', models.PositiveBigIntegerField(default=1, null=True)),
                ('number_of_feeders', models.PositiveSmallIntegerField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoadSheddingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, null=True)),
                ('feeders', models.ManyToManyField(related_name='loadshedding_feeders', to='base.feeder')),
            ],
        ),
        migrations.AddField(
            model_name='feeder',
            name='substation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feeder_lines', to='base.substation'),
        ),
    ]