# Generated by Django 5.0.6 on 2024-09-28 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='legislators.legislator'),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
