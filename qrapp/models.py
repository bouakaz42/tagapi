from django.db import models
from account.models import NewUser

# Create your models here.


class Email(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class vcard(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    organization = models.CharField(max_length=100,blank=True,null=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)

class Color(models.Model):
    background_color = models.CharField(max_length=30 , blank=True,null=True)
    foreground_color = models.CharField(max_length=30 ,blank=True,null=True)



class Qrcode(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    qr_name = models.CharField(max_length=100)
    domain_name = models.CharField(max_length=100)
    text = models.TextField(null=True,blank=True)  
    colors = models.OneToOneField(Color, on_delete=models.CASCADE, blank=True,null=True)
    vcard = models.OneToOneField(vcard, on_delete=models.CASCADE, blank=True,null=True)
    link = models.URLField(blank=True,null=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    qr_image = models.ImageField(upload_to='qr_images',blank=True,null=True)

    def __str__(self):
        return self.qr_name
        