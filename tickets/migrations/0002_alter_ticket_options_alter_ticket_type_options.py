# Generated by Django 4.0.1 on 2022-01-20 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='ticket_type',
            options={'verbose_name': 'Ticket_type', 'verbose_name_plural': 'Ticket_types'},
        ),
    ]