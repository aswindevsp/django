# Generated by Django 4.2.5 on 2023-09-14 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0002_doctor_password_doctor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='disease',
        ),
    ]
