# Generated by Django 5.0 on 2023-12-19 04:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0003_dictionary_best_video_dictionary_num_videos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signvideo',
            name='uploaded_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='signvideo',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files/%(dictionary_name)s', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]