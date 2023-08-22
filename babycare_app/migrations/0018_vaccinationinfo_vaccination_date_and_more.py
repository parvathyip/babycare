# Generated by Django 4.2.2 on 2023-08-09 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babycare_app', '0017_alter_mother_pregnancy_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinationinfo',
            name='vaccination_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccinationinfo',
            name='vaccination_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccinationinfo',
            name='vaccination_to',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccinationinfo',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='babycare_app.worker'),
        ),
        migrations.DeleteModel(
            name='VaccinationDate',
        ),
    ]
