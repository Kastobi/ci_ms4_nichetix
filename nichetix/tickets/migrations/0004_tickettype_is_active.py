# Generated by Django 3.2.6 on 2021-09-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]