# Generated by Django 4.0.6 on 2022-10-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HouseListing', '0035_tenant_t_user_alter_tenant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacateNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacate_date', models.CharField(max_length=1000)),
                ('remarks', models.CharField(max_length=1000)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HouseListing.lease')),
            ],
        ),
    ]
