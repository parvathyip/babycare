# Generated by Django 4.2.2 on 2023-08-11 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babycare_app', '0018_vaccinationinfo_vaccination_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='mother',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='panchayat',
        ),
        migrations.AddField(
            model_name='food',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='babycare_app.worker'),
        ),
    ]
