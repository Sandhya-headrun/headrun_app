# Generated by Django 2.2.12 on 2022-06-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_eventphotos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventphotos',
            old_name='userid',
            new_name='event_id',
        ),
    ]