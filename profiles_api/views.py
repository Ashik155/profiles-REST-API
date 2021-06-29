from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from profiles_api import serializer
from profiles_api import models



class HelloApiView(APIView):
    '''Testing the api '''

    #defining which serializer class to use 
    print("assigning Serialize Class")
    serializer_class = serializer.HelloSerializer


    def get(self,request,format=None):
        sending_list = ['hello','ashik']
        return Response({'message':'hello', 'lst':sending_list})

    

    def post(self,request):
        #here we will retrive serializer first and validate if it is handling our predefined 
        #validation or not ( in this case name has to be not more than 10 char )
        print("Passing Data to that class Serialiazer")
        serializer = self.serializer_class(data=request.data)
        print("Passed Data, And Waiting to validate ")
        if serializer.is_valid():
            print("checking Validatation")
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            print("Validatedddd....")
            return Response({'message':message})
        else:
            print("Not Proper Input...")
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    #mostly for whole object update 
    def put(self,request,pk=None):
        '''Handle whole object update not partial'''
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        ''' handle partial updates... '''
        return Response({'metho':'Patch'})


    def delete(self,request,pk=None):
        return Response({'Ofc':'delete'})




class HelloViewSet(viewsets.ViewSet):
    '''Just a testing a viewsets functionality '''

    serializer_class = serializer.HelloSerializer
    def list(self,request):
        list_to_send = ['ashik','patel','numbr of difffrent func']
        return Response({'msg':'hello','list ': list_to_send})
    

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f"hello {name}"
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        
    def retrieve(self,request, pk=None):
        '''Handle Getting an object by it's ID'''
        return Response({'method':'GET'})

    def update(self,request, pk=None):
        '''Handle updating an object by it's ID'''
        return Response({'method':'PUT'})
    
    def partial_update(self,request,pk=None):
        '''Handle partial updat of  an object by it's ID'''
        return Response({'method':'PATCH'})

    def destroy(self,request, pk=None):
        '''handle deleting that object by its id '''
        return Response ({'method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    '''creating and updating a new users '''
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

