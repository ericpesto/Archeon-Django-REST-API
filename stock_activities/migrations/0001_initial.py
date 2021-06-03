# Generated by Django 3.2 on 2021-05-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity_definitions', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockActivity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_date', models.DateTimeField(blank=True, null=True)),
                ('client_name', models.TextField(blank=True, null=True)),
                ('activity_amount_currency', models.TextField(blank=True, null=True)),
                ('activity_amount', models.FloatField(blank=True, null=True)),
                ('activity_comments', models.TextField(blank=True, null=True)),
                ('expense_currency', models.TextField(blank=True, null=True)),
                ('expense_pay_rate', models.FloatField(blank=True, null=True)),
                ('und_expense_amount', models.FloatField(blank=True, null=True)),
                ('acc_expense_amount', models.FloatField(blank=True, null=True)),
                ('activity_update_timestamp', models.DateTimeField(blank=True, null=True)),
                ('activity_type_id', models.ForeignKey(blank=True, db_column='activity_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='activity_definitions.activitydefinition')),
                ('stock_code', models.ForeignKey(blank=True, db_column='stock_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_activities', to='stock.stock')),
            ],
            options={
                'db_table': 'stockactivities',
            },
        ),
    ]