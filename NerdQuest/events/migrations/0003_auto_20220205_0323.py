# Generated by Django 2.2 on 2022-02-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20220204_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='creator',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
