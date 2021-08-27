from typing import Counter
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile

'''
post_save :- gives a notification when somethings is save or create in User models to show in Profile model too.
pre_save :- gives a notification when somethings wants to save in models.
'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username :
        username = f'{instance.first_name}_{instance.last_name}'.lower()
        counter = 1
        while User.objects.filter(username = username):
            counter += 1
            username = f'{instance.first_name}_{instance.last_name}_{counter}'
        instance.username = username
