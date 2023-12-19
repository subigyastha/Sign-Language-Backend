# Generated by Django 5.0 on 2023-12-19 04:33

import Videos.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0004_signvideo_uploaded_by_alter_signvideo_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signvideo',
            name='video_file',
            field=models.FileField(upload_to=Videos.models.video_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
