# Generated by Django 4.2.2 on 2023-08-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babycare_app', '0010_food_detail_desc_food_food_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='published_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
