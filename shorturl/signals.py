from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shorturl
from qrcode import *
from django.core.files import File
from io import BytesIO
from PIL import Image 

@receiver(post_save,sender=Shorturl)
def create_qr_image(sender ,instance, created,*args, **kwargs):
    print('signal captured')
    if created == True :
        print('qr image is null')
        qrimg = make(instance.short_url)
        qrbox = Image.new('RGB', (310, 310), 'white')
        qrbox.paste(qrimg)
        stream =BytesIO()
        qrbox.save(stream, format='PNG')
        instance.qr_image.save(instance.origin_url , File(stream) , save=False)
        qrbox.close()
        instance.save()

