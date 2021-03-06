# Generated by Django 3.2.3 on 2021-05-24 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210524_0220'),
        ('stock_links', '0004_alter_stocklink_stock_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklink',
            name='stock_code',
            field=models.ForeignKey(blank=True, db_column='stock_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_links', to='stock.stock'),
        ),
    ]
