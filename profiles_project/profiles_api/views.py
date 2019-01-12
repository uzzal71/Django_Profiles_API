from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .import serializers

# Create your views here.
class HelloAPIView(APIView):
    ''' Test API View '''
    
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' Returns a list of API features'''

        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ create a hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object. """
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provide in the request """
        return Response({'method': 'Patch'}) 

    def delete(self, request, pk=None):
        """ Deletes and objects. """    
        return Response({'method': 'Delete'})               