# Generated by Django 3.1.7 on 2021-03-24 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('medicine_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.TextField()),
                ('medicine_name', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineSupplier',
            fields=[
                ('supplier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.TextField()),
                ('contact_number', models.IntegerField()),
                ('address', models.TextField()),
                ('medicine_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicine.medicines')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineShops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField()),
                ('shop_email', models.TextField()),
                ('shop_location', models.TextField()),
                ('medicine_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicine.medicines')),
            ],
        ),
    ]
