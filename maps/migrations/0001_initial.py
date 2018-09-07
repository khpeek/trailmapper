# Generated by Django 2.1.1 on 2018-09-05 04:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('northeast', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('southwest', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
