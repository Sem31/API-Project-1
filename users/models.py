import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.deconstruct import deconstructible

# Create your models here.


'''
@deconstructible, In Django use for the class 'GenerateProfileImagePath' taken by django and be converted in migration.

this decorator is use for to include this class to when its migrate.
'''
@deconstructible  
class GenerateProfileImagePath(object):
    
    def __init__(self) -> None:
        pass

    '''
    instance is define for Profile class, because image is in Profile class why,
    we can use 'instance.user.id'
    '''
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]  # get the file extension.
        path = f'media/accounts/{instance.user.id}/images/'
        name = f'profile_image.{ext}'
        return os.path.join(path, name)

user_profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null= True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'