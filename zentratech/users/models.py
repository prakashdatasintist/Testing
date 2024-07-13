from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, unique=True)
    # Add any other fields you need for the profile here

    def __str__(self):
        return self.user.username

# # Signal to create or update the user profile
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
# @receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Ensure mobile_number uniqueness
        if Profile.objects.filter(mobile_number=instance.profile.mobile_number).exists():
            # Handle duplicate mobile_number, perhaps raise an error or log it
            pass
        else:
            Profile.objects.create(user=instance, mobile_number=instance.profile.mobile_number)
    instance.profile.save()