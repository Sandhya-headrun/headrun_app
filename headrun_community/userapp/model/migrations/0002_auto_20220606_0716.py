# Generated by Django 2.2.12 on 2022-06-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]