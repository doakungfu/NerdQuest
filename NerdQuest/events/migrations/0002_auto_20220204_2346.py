# Generated by Django 2.2 on 2022-02-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='type',
            new_name='gameType',
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ManyToManyField(to='events.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='created_by',
            field=models.ManyToManyField(to='events.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='start',
            field=models.TimeField(auto_now=True),
        ),
    ]
