# Generated by Django 3.2.8 on 2021-10-17 06:54

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedinformation',
            name='kind',
            field=models.CharField(choices=[('password', 'password'), ('time', 'time'), ('datetime-local', 'date and time'), ('tel', 'phone number'), ('number', 'number'), ('url', 'website link'), ('text', 'text'), ('email', 'email'), ('date', 'date')], max_length=150),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('code', models.CharField(default=events.models.ticketCodeGen, editable=False, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.event')),
                ('ticket_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.ticketclass')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='RequestedInformationAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=150)),
                ('requested_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='events.requestedinformation')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_information_answers', to='events.ticket')),
            ],
            options={
                'verbose_name': 'Extra info answer',
                'verbose_name_plural': 'Extra info answers',
            },
        ),
    ]
