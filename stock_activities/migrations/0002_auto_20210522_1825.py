# Generated by Django 3.2 on 2021-05-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockactivity',
            name='activity_type_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockactivity',
            name='stock_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]