# Generated by Django 4.2.2 on 2023-08-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babycare_app', '0022_worker_panchayat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='ward',
            field=models.CharField(max_length=30),
        ),
    ]
