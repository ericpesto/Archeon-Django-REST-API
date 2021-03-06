# Generated by Django 3.2.4 on 2021-06-05 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_auto_20210605_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.ForeignKey(blank=True, db_column='category_parent', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='categories.category'),
        ),
    ]
