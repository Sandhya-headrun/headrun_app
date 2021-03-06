# Generated by Django 2.2.12 on 2022-06-06 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_auto_20220606_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='photos',
        ),
        migrations.AddField(
            model_name='events',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
