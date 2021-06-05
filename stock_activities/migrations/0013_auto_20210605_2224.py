# Generated by Django 3.2.4 on 2021-06-05 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_definitions', '0007_alter_activitydefinition_activity_type_id'),
        ('stock', '0009_auto_20210605_2224'),
        ('stock_activities', '0012_auto_20210605_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockactivity',
            name='activity_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
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
