from django.db import models
from django.contrib.auth.models import User

# ✅ PROFILE MODEL (ONLY THIS)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='user')

    def __str__(self):
        return self.user.username


# ✅ AUTO CREATE PROFILE
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)