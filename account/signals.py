from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_token(sender ,instance=None, created=False,*args, **kwargs):
    if created :
        Token.objects.create(user=instance)
