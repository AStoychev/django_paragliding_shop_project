# Generated by Django 4.1.3 on 2022-11-11 09:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_harness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('model', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('image_url', models.URLField(max_length=1000, verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('type', models.CharField(choices=[('Standard', 'Standard'), ('Light', 'Light')], max_length=8)),
                ('year', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=4)),
            ],
        ),
    ]