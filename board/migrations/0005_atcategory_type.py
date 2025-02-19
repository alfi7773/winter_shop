# Generated by Django 5.1.4 on 2025-02-19 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_product_price_atcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='atcategory',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='at_category', to='board.type', verbose_name='выберите тип'),
            preserve_default=False,
        ),
    ]
