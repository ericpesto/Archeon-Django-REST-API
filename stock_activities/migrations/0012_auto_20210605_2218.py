# Generated by Django 3.2.4 on 2021-06-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_activities', '0011_auto_20210605_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockactivity',
            name='activity_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stockactivity',
            name='activity_type_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockactivity',
            name='stock_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
