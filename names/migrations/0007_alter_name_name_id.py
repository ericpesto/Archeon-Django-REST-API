# Generated by Django 3.2.4 on 2021-06-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0006_alter_name_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
