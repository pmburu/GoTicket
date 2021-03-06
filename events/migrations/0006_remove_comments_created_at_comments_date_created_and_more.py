# Generated by Django 4.0.1 on 2022-01-30 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_ticket_number_of_tickets'),
        ('events', '0005_rename_user_event_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='created_at',
        ),
        migrations.AddField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_comments', to='tickets.ticket'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendee_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendeee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attending', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending_event', to='events.event')),
            ],
        ),
    ]
