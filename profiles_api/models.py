from django.db import models

#these two  are important to overrride django by defualt user or usrr AuthenticationMiddleware system
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models.deletion import CASCADE

class UserProfileManager(BaseUserManager):
    '''Creating A normal User '''

    def create_user(self,email,name,password=None):
        '''creating a normal user'''
        if not email:
            raise ValueError("User Must have an email address....")
        #normalizing User...
        email = self.normalize_email(email)

        #not sure why ?
        user =  self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,name,password):
        '''creating a new superuser'''
        user = self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff= True
        user.save(using=self._db)

        return user








class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Databse model for users in the System """

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    #idontknow why ? ( this is being used while creating a new user using create function in searilizer)
    objects = UserProfileManager()

    #mentioning or here we are overrriding django user Authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    #mentining few ability to UserProfile

    def getFullName(self):
        '''Retrieve Full name '''
        return self.name

    def getShortName(self):
        '''retrive short name of user '''
        return self.name 

    def __str__(self):
        '''returnign String Representation of our user'''
        return self.email
    


class ProfileFeedItem(models.Model):
    '''Creatign a feed from profile where user can create and update things'''

    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    status_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        '''returoing sgtring representation of this obj'''
        return self.status_text
        
