# Generated by Django 3.2 on 2021-05-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(blank=True, db_column='type', max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('linked_file', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'names',
            },
        ),
    ]