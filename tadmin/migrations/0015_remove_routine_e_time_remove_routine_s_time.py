# Generated by Django 4.2.14 on 2024-10-10 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tadmin', '0014_rename_etime_routine_e_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='e_time',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='s_time',
        ),
    ]