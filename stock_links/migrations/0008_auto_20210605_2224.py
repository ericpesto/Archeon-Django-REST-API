# Generated by Django 3.2.4 on 2021-06-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_links', '0007_auto_20210605_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklink',
            name='link_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stocklink',
            name='stock_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]