# Generated by Django 4.1.3 on 2022-11-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_appuser_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]
