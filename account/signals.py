from django.db.models.signals import post_save
from django.contrib.auth.views import get_user_model
from django.dispatch import receiver



# from .models import Profile,User
#
#
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance,is_sender=True)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()