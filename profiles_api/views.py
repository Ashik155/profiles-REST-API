from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    '''Testing the api '''

    def get(self,request,format=None):
        sending_list = ['hello','ashik']
        return Response({'message':'hello', 'lst':sending_list})