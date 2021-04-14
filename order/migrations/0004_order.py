# Generated by Django 3.1.7 on 2021-04-09 17:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0011_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_remove_orderdetails_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('phone', models.CharField(default='', max_length=14)),
                ('address', models.TextField(default='')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
