# Generated by Django 4.0.1 on 2022-01-31 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_ticket_number_of_tickets_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tickettype',
            options={'verbose_name': 'Ticket Type', 'verbose_name_plural': 'Ticket Types'},
        ),
    ]