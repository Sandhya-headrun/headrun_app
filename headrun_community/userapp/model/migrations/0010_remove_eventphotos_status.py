# Generated by Django 2.2.12 on 2022-06-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_auto_20220606_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventphotos',
            name='status',
        ),
    ]
