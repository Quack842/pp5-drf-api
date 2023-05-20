# Generated by Django 3.2.18 on 2023-05-20 12:11

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20230520_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='camera_type',
            field=models.CharField(max_length=100, verbose_name=posts.models.CameraType),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_type',
            field=models.CharField(max_length=100, verbose_name=posts.models.PhotoType),
        ),
    ]
