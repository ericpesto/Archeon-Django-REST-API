# Generated by Django 3.2.4 on 2021-06-05 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0007_alter_name_name_id'),
        ('categories', '0009_auto_20210605_2224'),
        ('stock', '0008_auto_20210605_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='artist_id',
            field=models.ForeignKey(blank=True, db_column='artist_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_stock', to='names.name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buyer_id',
            field=models.ForeignKey(blank=True, db_column='buyer_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_stock', to='names.name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category_id',
            field=models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='location_id',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_stock', to='names.name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='partner_id',
            field=models.ForeignKey(blank=True, db_column='partner_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_stock', to='names.name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='source_id',
            field=models.ForeignKey(blank=True, db_column='source_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_stock', to='names.name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sub_category_1_id',
            field=models.ForeignKey(blank=True, db_column='sub_category_1_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category_1', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sub_category_2_id',
            field=models.ForeignKey(blank=True, db_column='sub_category_2_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category_2', to='categories.category'),
        ),
    ]
