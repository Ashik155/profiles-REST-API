from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from profiles_api import serializer



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