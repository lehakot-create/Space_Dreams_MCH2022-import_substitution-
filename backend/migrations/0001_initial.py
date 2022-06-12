# Generated by Django 4.0.5 on 2022-06-05 17:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_company', models.IntegerField(null=True, unique=True)),
                ('Company', models.CharField(max_length=128)),
                ('Direction', models.CharField(max_length=512)),
                ('Description', models.TextField(null=True)),
                ('Categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), null=True, size=None)),
                ('Products', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), null=True, size=None)),
                ('Status', models.CharField(max_length=128)),
                ('INN', models.BigIntegerField(null=True)),
                ('OGRN', models.BigIntegerField(null=True)),
                ('KPP', models.BigIntegerField(null=True)),
                ('Entity', models.CharField(max_length=128, null=True)),
                ('Employ_number', models.IntegerField(null=True)),
                ('Region', models.CharField(max_length=128, null=True)),
                ('Locality', models.CharField(max_length=128, null=True)),
                ('Address', models.CharField(max_length=128, null=True)),
                ('Telephone', models.CharField(max_length=128, null=True)),
                ('Post', models.CharField(max_length=128, null=True)),
                ('URL', models.CharField(max_length=128, null=True)),
                ('VK', models.CharField(max_length=128, null=True)),
                ('Instagram', models.CharField(max_length=128, null=True)),
                ('Facebook', models.CharField(max_length=128, null=True)),
                ('Youtube', models.CharField(max_length=128, null=True)),
                ('Catalogs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128, null=True), size=None)),
            ],
        ),
    ]