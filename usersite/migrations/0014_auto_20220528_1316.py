# Generated by Django 3.2.13 on 2022-05-28 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0013_remove_dayeventmodel_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayarticlemodel',
            old_name='parent_event',
            new_name='parent_event_time',
        ),
        migrations.RenameField(
            model_name='dayaudiomodel',
            old_name='parent_event',
            new_name='parent_event_time',
        ),
        migrations.RenameField(
            model_name='dayphotomodel',
            old_name='parent_event',
            new_name='parent_event_time',
        ),
        migrations.RenameField(
            model_name='dayvideomodel',
            old_name='parent_event',
            new_name='parent_event_time',
        ),
    ]
