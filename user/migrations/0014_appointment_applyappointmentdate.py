# Generated by Django 3.1.7 on 2021-04-11 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20210401_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='applyAppointmentDate',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
