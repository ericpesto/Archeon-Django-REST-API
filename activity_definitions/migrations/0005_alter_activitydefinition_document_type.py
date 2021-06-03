# Generated by Django 3.2 on 2021-05-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document_statements', '0001_initial'),
        ('activity_definitions', '0004_alter_activitydefinition_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydefinition',
            name='document_type',
            field=models.ForeignKey(blank=True, db_column='document_type', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='document_statements.documentstatement'),
        ),
    ]
