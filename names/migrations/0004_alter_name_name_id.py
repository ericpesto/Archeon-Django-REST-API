# Generated by Django 3.2.4 on 2021-06-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0003_alter_name_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
