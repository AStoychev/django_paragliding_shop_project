# Generated by Django 4.1.3 on 2022-11-11 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('model', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('image_url', models.URLField(max_length=1000, verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('en_certification', models.CharField(choices=[('EN_A', 'EN A'), ('EN_B', 'EN B'), ('EN_C', 'EN C'), ('EN_D', 'EN D'), ('Tandem', 'Tandem wings'), ('Acro', 'Acro wings'), ('Speedwings', 'Speedwings')], max_length=10)),
                ('year', models.DateField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=4)),
                ('test', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('porosity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(10)])),
            ],
        ),
    ]
