from email.mime import image
import os
from django.db import models
from django.contrib.auth.models import User

from django.utils.deconstruct import deconstructible

@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'mdia/accounts/{instance.user.id}/images'
        name = f'porfile_image.{ext}'
        return os.path.join(path, name)

User_profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=User_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\' Profile'
