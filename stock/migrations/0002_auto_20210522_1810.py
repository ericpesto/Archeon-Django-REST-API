# Generated by Django 3.2 on 2021-05-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sub_category_1_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sub_category_2_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
