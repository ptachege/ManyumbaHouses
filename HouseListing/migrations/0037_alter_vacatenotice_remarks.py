# Generated by Django 4.0.6 on 2022-10-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseListing', '0036_vacatenotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacatenotice',
            name='remarks',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
