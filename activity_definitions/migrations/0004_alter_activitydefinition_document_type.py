# Generated by Django 3.2 on 2021-05-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_definitions', '0003_alter_activitydefinition_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydefinition',
            name='document_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]
