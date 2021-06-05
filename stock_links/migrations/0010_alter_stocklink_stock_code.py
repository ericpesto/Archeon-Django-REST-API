# Generated by Django 3.2.4 on 2021-06-05 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20210605_2224'),
        ('stock_links', '0009_alter_stocklink_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklink',
            name='stock_code',
            field=models.ForeignKey(blank=True, db_column='stock_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_links', to='stock.stock'),
        ),
    ]