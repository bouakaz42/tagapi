from django.db import models
import uuid
# Create your models here.


class Shorturl(models.Model):
    origin_url = models.CharField(max_length = 500 , verbose_name='Put Your Link Here')
    short_url = models.CharField(max_length=10 , null=True , blank = True) 
    qr_image = models.ImageField(upload_to='qr_link_image', blank=True)
    # overide save method
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = str(uuid.uuid4())[:6]
      
        super(Shorturl, self).save(*args, **kwargs)
