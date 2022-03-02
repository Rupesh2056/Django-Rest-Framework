from django.shortcuts import render,get_object_or_404
from .models import Album
from django.http import HttpResponse , JsonResponse 
from .serializer import AlbumSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter


# Create your views here.

#function based view serialization

@api_view(['Get','POST'])
def ListAlbum(request):
    try:
        albums = Album.objects.all()
    except Album.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = AlbumSerializer(albums,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST':
        article = JSONParser().parse(request)
        serializer = AlbumSerializer(data = article)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status = status.HTTP_201_CREATED)
        return HttpResponse(status = status.HTTP_400_BAD_REQUEST)

@api_view(['Get','PUT','DELETE'])
def DetailAlbum(request,pk):
    try:
        album = Album.objects.get(pk=pk)
        
    except Album.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data,status=200)

    if request.method == 'PUT':
        serializer = AlbumSerializer(instance=album , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method  == 'DELETE':
        album.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)


# Class based view => Inherits from APIView and simply defines the methods 
class AlbumClassApi(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return HttpResponse(status = status.HTTP_400_BAD_REQUEST)

class DetailAlbumApi(APIView):
    def get_album(self,pk):
        try:
            return Album.objects.get(id=pk)
        except Album.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        album = self.get_album(pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        album = self.get_album(pk)
        serializer = AlbumSerializer(instance = album,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return HttpResponse(status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        album = self.get_album(pk)
        album.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#Generic view where the class inherits from gererics.GenericAPIView and user mixins for simplicity or use basic genericis.ListCreateApiView

class GenericApi(generics.GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self,request,pk=None):
        if pk:       
            return self.retrieve(request,pk)
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)



class ViewsetApi(viewsets.ViewSet):
    def list(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk):
        albums = Album.objects.all()
        album = get_object_or_404(albums,pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data,status=status.HTTP_200_OK)


    
    

    
    



        

        


    

        
