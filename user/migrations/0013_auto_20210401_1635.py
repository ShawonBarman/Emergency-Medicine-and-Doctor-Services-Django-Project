# Generated by Django 3.1.7 on 2021-04-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210331_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
