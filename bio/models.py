from django.db import models
from account.models import NewUser
# Create your models here.

#write a Content class that have these fields heading text divider links html image rss_feed news_letter contact_form vCard product youtube_link whatsapp_info
class vCard(models.Model):  
    first_name=models.CharField(max_length=150,blank=True,null=True)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    phone_number = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField(max_length=150,blank=True,null=True)
    site = models.CharField(max_length=150,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    state = models.CharField(max_length=150,blank=True,null=True)
    country = models.CharField(max_length=150,blank=True,null=True)

class Link(models.Model):
    font_aws_class = models.CharField(max_length=150,blank=True,null=True)
    text = models.CharField(max_length=150,blank=True,null=True)
    link = models.CharField(max_length=150,blank=True,null=True)
    color = models.CharField(max_length=150,blank=True,null=True)
    background_color = models.CharField(max_length=150,blank=True,null=True)
    style = models.CharField(max_length=150,blank=True,null=True)

class Contactform(models.Model):
    text = models.TextField(max_length=300,blank=True,null=True)
    email = models.EmailField(max_length=150,blank=True,null=True)


    def __str__(self):
        return self.text
    
   
class Product(models.Model):
    name = models.CharField(max_length=150,blank=True,null=True)
    price = models.CharField(max_length=150,blank=True,null=True)
    description = models.TextField(max_length=300,blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    link = models.CharField(max_length=150,blank=True,null=True) 

    def __str__(self):
        return self.name


class Heading(models.Model):
    text = models.TextField(max_length=300,blank=True,null=True)
    color = models.CharField(max_length=150,blank=True,null=True)


class Content(models.Model):
    heading = models.OneToOneField(Heading,on_delete=models.CASCADE , blank=True,null=True)
    text = models.CharField(max_length=150,blank=True,null=True)
    link = models.OneToOneField(Link,on_delete=models.CASCADE,blank=True,null=True)
    html = models.TextField(max_length=300,blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    rss_feed = models.CharField(max_length=150,blank=True,null=True)
    news_letter = models.CharField(max_length=150,blank=True,null=True)
    contact_form = models.OneToOneField(Contactform,on_delete=models.CASCADE,blank=True,null=True)
    vcard = models.OneToOneField(vCard,on_delete=models.CASCADE,blank=True,null=True)
    product = models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True)
    youtube_link = models.CharField(max_length=150,blank=True,null=True)
    apple_music = models.CharField(max_length=150,blank=True,null=True)
    whatsapp_number = models.CharField(max_length=150,blank=True,null=True)
    spotify_link = models.CharField(max_length=150,blank=True,null=True)
    








class Sociallinks(models.Model):
    # for ever social media site write a charfield with blank=True,null=True and max_length=220
    facebook = models.CharField(max_length=220,blank=True,null=True)
    twitter = models.CharField(max_length=220,blank=True,null=True)
    instagram = models.CharField(max_length=220,blank=True,null=True)
    linkedin = models.CharField(max_length=220,blank=True,null=True)
    youtube = models.CharField(max_length=220,blank=True,null=True)
    telegram = models.CharField(max_length=220,blank=True,null=True)
    pinterest = models.CharField(max_length=220,blank=True,null=True)
    snapchat = models.CharField(max_length=220,blank=True,null=True)
    discourd = models.CharField(max_length=220,blank=True,null=True)
    twitch = models.CharField(max_length=220,blank=True,null=True)
    shopify = models.CharField(max_length=220,blank=True,null=True)
    amazon = models.CharField(max_length=220,blank=True,null=True)


class Advanced(models.Model):
    meta_title = models.CharField(max_length=150,blank=True,null=True)
    meta_description = models.TextField(max_length=400,blank=True,null=True)
    password_bio = models.CharField(max_length=150,blank=True,null=True)
    custom_css = models.TextField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.meta_title


class Appearance(models.Model):
    bg_color = models.CharField(max_length=150,blank=True,null=True)
    font = models.CharField(max_length=150,blank=True,null=True)
    text_color = models.CharField(max_length=150,blank=True,null=True)
    btn_color = models.CharField(max_length=150,blank=True,null=True)


class Bio(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=150,blank=True,null=True)
    page_alias = models.CharField(max_length=150,blank=True,null=True,unique=True)
    image = models.ImageField(upload_to='images/bio_img/',blank=True,null=True)
    content = models.OneToOneField(Content , on_delete=models.CASCADE , blank=True,null=True)
    social_links = models.OneToOneField(Sociallinks , on_delete=models.CASCADE, blank=True,null=True)
    advanced = models.OneToOneField(Advanced , on_delete=models.CASCADE, blank=True,null=True)
    appearance = models.OneToOneField(Appearance , on_delete=models.CASCADE, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_name