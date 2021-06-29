from django.db.models import fields
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    '''Serialzing means converting i/p from python to api or api to python '''
    print("Entering to serialize request...")
    name = serializers.CharField(max_length=12)



class UserProfileSerializer(serializers.ModelSerializer):
    ''' Serializes a user Profile objet '''
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')

        #we are adding this thing because we dont want to show password while get or retrive methods
        extra_kwargs = {
            'password': {
                'write_only' : True,
                'style' : {'input_type':'password'}
            }
        }



    def create(self,validated_data):
        '''create and return a new user'''
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'])

        return user