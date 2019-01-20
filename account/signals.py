from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, MedicalInfo
   

@receiver(post_save, sender=User)
def medical_info_create(sender, instance, created, **kwargs):
    if created:
        MedicalInfo.objects.create(patient=instance)
    instance.medical_info.save()