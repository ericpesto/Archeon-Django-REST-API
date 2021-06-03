# Generated by Django 3.2.3 on 2021-05-24 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210524_0220'),
        ('activity_definitions', '0006_alter_activitydefinition_document_type'),
        ('stock_activities', '0008_auto_20210524_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockactivity',
            name='activity_type_id',
            field=models.ForeignKey(blank=True, db_column='activity_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='activity_definitions.activitydefinition'),
        ),
        migrations.AlterField(
            model_name='stockactivity',
            name='stock_code',
            field=models.ForeignKey(blank=True, db_column='stock_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_activities', to='stock.stock'),
        ),
    ]