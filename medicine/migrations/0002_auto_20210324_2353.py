# Generated by Django 3.1.7 on 2021-03-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicineshops',
            old_name='medicine_id',
            new_name='medicine',
        ),
        migrations.RenameField(
            model_name='medicinesupplier',
            old_name='medicine_id',
            new_name='medicine',
        ),
    ]
