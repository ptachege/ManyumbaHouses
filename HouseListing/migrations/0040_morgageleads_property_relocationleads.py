# Generated by Django 4.0.6 on 2022-10-28 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HouseListing', '0039_remove_invoice_apartment_remove_invoice_house_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='morgageleads',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HouseListing.properties'),
        ),
        migrations.CreateModel(
            name='RelocationLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank='True', max_length=100, null=True)),
                ('phone', models.CharField(blank='True', max_length=100, null=True)),
                ('email', models.CharField(blank='True', max_length=100, null=True)),
                ('employment_type', models.CharField(blank='True', max_length=100, null=True)),
                ('gross_income', models.CharField(blank='True', max_length=100, null=True)),
                ('convinient_time', models.CharField(blank='True', max_length=100, null=True)),
                ('property_rent', models.IntegerField(blank='True', null=True)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HouseListing.properties')),
            ],
            options={
                'verbose_name': 'RelocationLeads',
                'verbose_name_plural': 'RelocationLeads',
            },
        ),
    ]
