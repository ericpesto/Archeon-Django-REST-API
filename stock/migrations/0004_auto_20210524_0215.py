# Generated by Django 3.2.3 on 2021-05-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20210522_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='artist_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='location_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='partner_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='source_id',
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
