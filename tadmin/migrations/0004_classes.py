# Generated by Django 4.2.14 on 2024-08-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadmin', '0003_alter_routine_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
