from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    best_video = models.OneToOneField('SignVideo', on_delete=models.SET_NULL, null=True, blank=True)
    num_videos = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def pre_save_dictionary(sender, instance, **kwargs):
    if instance.pk:
        original_instance = Dictionary.objects.get(pk=instance.pk)
        if original_instance.best_video != instance.best_video:
            # Uncheck is_best for the old best_video
            if original_instance.best_video:
                original_instance.best_video.is_best = False
                original_instance.best_video.save(update_fields=['is_best'])


def video_upload_path(instance, filename):
    # Check if the dictionary_name is set
    if instance.dictionary_name:
        dictionary_name = instance.dictionary_name
    else:
        # Handle the case where dictionary_name is not set
        dictionary_name = 'unknown'

    return f'uploads/video_files/{dictionary_name}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


class SignVideo(models.Model):
    dictionary_name = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to=video_upload_path, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    uploaded_by = models.CharField(max_length=255,blank=True, null=True)
    is_best = models.BooleanField(default=False)
    converted_numpy = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # If the video is marked as the best, update the best_video link in the dictionary
        if self.is_best:
            self.dictionary_name.best_video = self
            # Uncheck is_best for any existing best video in the dictionary
            SignVideo.objects.filter(dictionary_name=self.dictionary_name, is_best=True).exclude(pk=self.pk).update(is_best=False)
            self.dictionary_name.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dictionary_name} - {self.video_file}"

@receiver(post_save, sender=SignVideo)
def update_num_videos(sender, instance, **kwargs):
    dictionary_name = instance.dictionary_name
    num_videos = SignVideo.objects.filter(dictionary_name=dictionary_name).count()
    Dictionary.objects.filter(id=dictionary_name.id).update(num_videos=num_videos)

    if num_videos > 0 and instance.is_best:
        # If there are videos and the video is marked as the best, update the best_video link in the dictionary
        instance.dictionary_name.best_video = instance
        # Uncheck is_best for any existing best video in the dictionary
        SignVideo.objects.filter(dictionary_name=dictionary_name, is_best=True).exclude(pk=instance.pk).update(is_best=False)
        instance.dictionary_name.save(update_fields=['best_video'])

