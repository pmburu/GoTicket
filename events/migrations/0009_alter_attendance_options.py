# Generated by Django 4.0.1 on 2022-01-30 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_rename_attendeee_attendance_attendee_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendances'},
        ),
    ]