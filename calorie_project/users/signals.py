# get post_save signal when user is created
from django.db.models.signals import post_save
# user model is the sender which is what is sending the signal
from django.contrib.auth.models import User
# receiver: gets signal and performs a task
from django.dispatch import receiver
# profile
from . models import Profile


# **kwargs accepts any additional args
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # runs everytime user is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()



