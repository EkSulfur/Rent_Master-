# Generated by Django 5.0 on 2023-12-18 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='owner_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='available_from',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='lease_terms',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='leaserecord',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting_logs.house'),
        ),
        migrations.AlterField(
            model_name='leaserecord',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting_logs.tenant'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Landlord',
        ),
    ]
