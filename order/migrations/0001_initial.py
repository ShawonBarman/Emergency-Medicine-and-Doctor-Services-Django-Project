# Generated by Django 3.1.7 on 2021-03-24 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('order_date', models.CharField(max_length=10)),
                ('delivery_date', models.CharField(max_length=10)),
                ('medicine_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicines')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]