# Generated by Django 4.0.1 on 2022-01-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_options_alter_ticket_type_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='number_of_tickets',
            field=models.IntegerField(default=0),
        ),
    ]