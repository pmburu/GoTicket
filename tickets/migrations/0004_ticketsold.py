# Generated by Django 4.0.1 on 2022-01-31 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_number_of_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketSold',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Ticket Sold',
                'verbose_name_plural': 'Tickets Sold',
            },
        ),
    ]