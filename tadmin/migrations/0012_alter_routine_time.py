# Generated by Django 4.2.14 on 2024-10-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadmin', '0011_routine_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='time',
            field=models.TimeField(default='6:0:0'),
        ),
    ]