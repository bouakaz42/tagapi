from django.contrib import admin
from .models import *
# Register your models here.
# register all the models that i import from .models
admin.site.register(Bio)
admin.site.register(Product)
admin.site.register(Heading)
admin.site.register(Content)
admin.site.register(Link)
admin.site.register(Contactform)
admin.site.register(vCard)
admin.site.register(Sociallinks)
admin.site.register(Appearance)
admin.site.register(Advanced)

