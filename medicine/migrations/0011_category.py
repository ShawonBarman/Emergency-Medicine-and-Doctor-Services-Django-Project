# Generated by Django 3.1.7 on 2021-04-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_auto_20210331_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
