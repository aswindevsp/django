# Generated by Django 4.2.5 on 2023-09-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0005_patient_doctorname_alter_doctor_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='consultation',
            field=models.TextField(default='No consultation yet'),
        ),
    ]