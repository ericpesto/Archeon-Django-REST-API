# Generated by Django 3.2.3 on 2021-05-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
