# Generated by Django 3.2.6 on 2021-09-01 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_alter_song_uploaded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
