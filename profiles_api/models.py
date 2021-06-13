from django.db import models

#these two  are important to overrride django by defualt user or usrr AuthenticationMiddleware system
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''Creating A normal User '''

    def create_user(self,email,name,password=None):
        '''creating a normal user'''
        if not email:
            raise ValueError("User Must have an email address....")
        
        email = self.normalize_email(email)
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


    #idontknow why ?
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