# Generated by Django 4.2.6 on 2023-11-10 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-time',)},
        ),
    ]
