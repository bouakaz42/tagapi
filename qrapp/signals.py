from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import Qrcode
from qrcode import *
from PIL import Image
from io import BytesIO
from django.core.files import File



@receiver(post_save,sender=Qrcode)
def create_token(sender ,instance=None, created=False,*args, **kwargs):
    if created :
        qrimg = make(instance.qr_name)
        qrbox = Image.new('RGB', (310, 310), 'white')
        qrbox.paste(qrimg)
        stream =BytesIO()
        qrbox.save(stream, format='PNG')
        instance.qr_image.save(instance.qr_name , File(stream) , save=False)
        qrbox.close()
        instance.save()

