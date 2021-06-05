# Generated by Django 3.2.4 on 2021-06-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_alter_category_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]