# Generated by Django 4.0.1 on 2022-01-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_alter_ticketcart_options_remove_ticketcart_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
