# Generated by Django 4.2.2 on 2023-08-07 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babycare_app', '0002_availablevaccination_healthcentre_panchayat_scheme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='panchayat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='babycare_app.panchayat'),
        ),
    ]
