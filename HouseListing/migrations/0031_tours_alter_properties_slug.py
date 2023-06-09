# Generated by Django 4.0.6 on 2022-10-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseListing', '0030_userprofile_account_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank='True', max_length=100, null=True)),
                ('phone', models.CharField(blank='True', max_length=100, null=True)),
                ('tour_date', models.CharField(blank='True', max_length=100, null=True)),
                ('message', models.CharField(blank='True', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tours',
                'verbose_name_plural': 'Tours',
            },
        ),
    ]
