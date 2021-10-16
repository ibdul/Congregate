# Generated by Django 3.2.8 on 2021-10-16 21:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('code', models.CharField(default=events.models.eventCodeGen, editable=False, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('kind', models.CharField(max_length=15)),
                ('venue', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('max_guests', models.PositiveIntegerField(blank=True, null=True)),
                ('account', models.PositiveIntegerField(blank=True, null=True)),
                ('refundable', models.BooleanField(default=False)),
                ('refund_deadline', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('pass_code', models.CharField(blank=True, default=events.models.passCodeGen, max_length=50)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='TicketClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_classes', to='events.event')),
            ],
            options={
                'verbose_name': 'Ticket class',
                'verbose_name_plural': 'Ticket classes',
            },
        ),
        migrations.CreateModel(
            name='RequestedInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('kind', models.CharField(choices=[('datetime-local', 'date and time'), ('number', 'number'), ('time', 'time'), ('date', 'date'), ('text', 'text'), ('url', 'website link'), ('tel', 'phone number'), ('password', 'password'), ('email', 'email')], max_length=150)),
                ('maxlength', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('required', models.BooleanField(default=False)),
                ('short_description', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_Information', to='events.event')),
            ],
            options={
                'verbose_name': 'requested information',
                'verbose_name_plural': 'requested information',
            },
        ),
    ]
