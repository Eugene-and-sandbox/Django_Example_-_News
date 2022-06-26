# Generated by Django 3.2.13 on 2022-05-28 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0016_alter_dayeventmodel_event_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayarticlemodel',
            name='parent_event_time',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='usersite.dayeventmodel'),
        ),
        migrations.AlterField(
            model_name='dayaudiomodel',
            name='parent_event_time',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='usersite.dayeventmodel'),
        ),
        migrations.AlterField(
            model_name='dayeventmodel',
            name='event_preview',
            field=models.ImageField(blank=True, default='default_image.png', upload_to='media/images/event_preview/'),
        ),
        migrations.AlterField(
            model_name='dayphotomodel',
            name='parent_event_time',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='usersite.dayeventmodel'),
        ),
        migrations.AlterField(
            model_name='dayvideomodel',
            name='parent_event_time',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='usersite.dayeventmodel'),
        ),
    ]
