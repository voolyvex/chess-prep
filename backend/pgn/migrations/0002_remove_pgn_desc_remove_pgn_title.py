# Generated by Django 4.1.7 on 2023-02-28 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pgn',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='pgn',
            name='title',
        ),
    ]