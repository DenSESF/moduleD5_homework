# Generated by Django 4.2.6 on 2023-10-26 10:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DRNK', 'Drink'), ('BRGR', 'Burger'), ('SNCK', 'Snack'), ('DSRT', 'Dessert')], default='BRGR', max_length=5)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField()),
            ],
        ),
    ]
