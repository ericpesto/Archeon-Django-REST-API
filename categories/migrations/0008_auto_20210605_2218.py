# Generated by Django 3.2.4 on 2021-06-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_auto_20210605_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
