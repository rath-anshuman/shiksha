# Generated by Django 4.2.14 on 2024-08-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadmin', '0006_delete_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.CharField(choices=[('CLASSDAY', 'CLASSDAY'), ('HOLIDAY', 'HOLIDAY'), ('EXAMS', 'EXAMS')], default='CLASSDAY')),
            ],
        ),
    ]