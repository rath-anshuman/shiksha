# Generated by Django 4.2.14 on 2024-10-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tadmin', '0013_rename_time_routine_stime_routine_etime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine',
            old_name='etime',
            new_name='e_time',
        ),
        migrations.RenameField(
            model_name='routine',
            old_name='stime',
            new_name='s_time',
        ),
    ]
