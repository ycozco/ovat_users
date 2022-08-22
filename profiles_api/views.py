from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers, models




class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request,pk=None):
        """maneja actualizacion de un objeto"""
        return Response({'method': 'PUT'})
    
    def patch(self,request,pk=None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})
    
    def delete(self,request,pk=None):
        """Dele an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """TEST APIT VIEW SET"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return mensaje hello world"""
        a_viewset = [
            'esto es un viewset (list, create,retrieve, update, partial_update',
            'Mapea automaticamente los URLSusando Routers',
        ]
        return Response({'message':'holl!','a_viewset':a_viewset})
    def create(self,request):
        """create new message hello world"""
        serializer = self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        """obtiene un objete y su id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """create and update profiles"""
    serializer = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    
