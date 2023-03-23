# Generated by Django 4.0.6 on 2022-09-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseListing', '0024_tenant_id_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='BusinessLounge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='properties',
            name='CCTV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='properties',
            name='Elevator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='properties',
            name='Majortransportlinks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='properties',
            name='MeetingRooms',
            field=models.BooleanField(default=False),
        ),
    ]
