# Generated by Django 3.1.7 on 2021-03-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20210331_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='schedule',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialist',
            field=models.CharField(max_length=50),
        ),
    ]