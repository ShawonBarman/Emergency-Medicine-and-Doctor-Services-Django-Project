# Generated by Django 3.1.7 on 2021-03-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20210331_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='strength',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
