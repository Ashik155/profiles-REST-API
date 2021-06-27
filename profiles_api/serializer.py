from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serialzing means converting i/p from python to api or api to python '''
    print("Entering to serialize request...")
    name = serializers.CharField(max_length=12)