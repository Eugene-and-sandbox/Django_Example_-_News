# Generated by Django 3.2.13 on 2022-05-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0004_alter_generaldaydescriptionmodel_daily_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Categores',
            },
        ),
        migrations.CreateModel(
            name='DayVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='media/video/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.itemcategorymodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.generaldaydescriptionmodel')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='DayPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='media/photo/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photocategory', to='usersite.itemcategorymodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.generaldaydescriptionmodel')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='DayAudioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='media/video/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.itemcategorymodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.generaldaydescriptionmodel')),
            ],
            options={
                'verbose_name': 'audio',
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='DayArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('article', models.FileField(upload_to='media/video/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.itemcategorymodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersite.generaldaydescriptionmodel')),
            ],
            options={
                'verbose_name': 'audio',
                'verbose_name_plural': 'Audios',
            },
        ),
    ]
