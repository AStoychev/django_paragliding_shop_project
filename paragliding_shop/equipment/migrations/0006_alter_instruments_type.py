# Generated by Django 4.1.3 on 2022-11-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_helmets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruments',
            name='type',
            field=models.CharField(choices=[('Varios', 'Varios'), ('AltiVarios', 'AltiVarios'), ('AltiVariosGPS', 'AltiVariosGPS')], max_length=13),
        ),
    ]
