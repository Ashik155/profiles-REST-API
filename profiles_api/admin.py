from django.contrib import admin
from profiles_api import models

# Register your models here.


#Registering USer Authentication model 
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)