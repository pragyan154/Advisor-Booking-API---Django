# Generated by Django 3.1.7 on 2021-04-30 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='userid',
        ),
    ]
