# Generated by Django 3.2.4 on 2021-06-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_definitions', '0006_alter_activitydefinition_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydefinition',
            name='activity_type_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]