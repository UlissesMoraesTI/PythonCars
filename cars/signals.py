from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print(f"Pre-saving car: {instance}")

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(f"Post-saving car: {instance}")

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print(f"Pre-deleting car: {instance}")

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print(f"Post-deleting car: {instance}")

