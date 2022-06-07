# Generated by Django 2.2.12 on 2022-06-06 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0005_auto_20220606_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='work_location',
            field=models.CharField(choices=[('BENGALURU', 'BENGALURU'), ('HYDERABAD', 'HYDERABAD')], default='HYDERABAD', max_length=30),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='reacted_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likedpost', to='userapp.Posts'),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=50, null=True)),
                ('event_descript', models.TextField(max_length=500, null=True)),
                ('photos', models.ImageField(null=True, upload_to='static/', verbose_name='EventPhotos')),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=500)),
                ('team', models.CharField(choices=[('HRH', 'HRH'), ('HRB', 'HRB')], default='HRH', max_length=20)),
                ('posted_username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_postedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
