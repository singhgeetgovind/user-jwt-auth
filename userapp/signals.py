from .models import CustomUser,Token
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=CustomUser)
def create(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
        print('Token is created')
    else:
        print('Token is not created')

@receiver(post_save, sender=CustomUser) 
def save_profile(sender, instance, **kwargs):
        instance.token.save()