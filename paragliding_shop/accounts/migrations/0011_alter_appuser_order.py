# Generated by Django 4.1.3 on 2022-11-30 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_appuser_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='order',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]