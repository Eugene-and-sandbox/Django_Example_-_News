# Generated by Django 3.2.13 on 2022-05-29 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0021_alter_dayaudiomodel_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitemslistmodel',
            name='date',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='usersite.generaldaydescriptionmodel'),
        ),
    ]
