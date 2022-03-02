from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .models import Band
from rest_framework.response import Response
from .serializer import BandSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
# Create your views here.

@api_view(['GET','POST'])
def DisplayBands(request):

    if request.method == 'GET':
        bands = Band.objects.all()
        serializer = BandSerializer(bands,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BandSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status = 400)

@api_view(['Get','PUT','DELETE'])
def DetailBand(request,id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = BandSerializer(band)
        print(serializer.data)
        return Response(serializer.data,status = 200)
    elif request.method == 'PUT':
        serializer = BandSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status = 400)
    elif request.method == 'DELETE':
        band.delete()
        return Response(status = 204)

# Class-based API views

class ClassApi(APIView):
    def get(self,request):
        bands = Band.objects.all()
        serializer = BandSerializer(bands,many=True)
        print(serializer.data)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status = 400)

class DetailClassApi(APIView):
    def getband(self,id):
        bands = Band.objects.all()
        return get_object_or_404(bands,id=id)
    
    def get(self,request,id):
        band = self.getband(id)
        serializer = BandSerializer(band)
        return Response(serializer.data)
    
    def put(self,request,id):
        band = self.getband(id)
        serializer = BandSerializer(instance = band,data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status = 400)

    def delete(self,request,id):
        band = self.getband(id)
        band.delete()
        return HttpResponse(status=204)


# Generic-view API


class GenericApi(generics.CreateAPIView,generics.ListAPIView):
     queryset=Band.objects.all()
     serializer_class = BandSerializer
    

class DetailGenericApi(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView): 
    queryset=Band.objects.all()
    serializer_class = BandSerializer
    lookup_field = 'id'
    # you can also override these list,retrieve,update... views as below

# class GenericApi(generics.ListAPIView,generics.RetrieveAPIView,generics.CreateAPIView):
#     queryset=Band.objects.all()
#     serializer_class = BandSerializer
    

#     def list(self,request):
#         bands = self.get_queryset()
#         serializer = BandSerializer(bands,many=True)
#         return Response(serializer.data)


#using mixins on GenericAPIView => need to define methods
class GenericApiMixins(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = BandSerializer
    queryset = Band.objects.all()

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class DetailGenericApiMixins(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    def update(self,request,id):
        return self.update(request,id)
    def delete(self,request,id):
        return self.delete(request,id)
    def retrieve(self,request,id):
        return self.retrieve(request,id)


#using viewset and router => same as classbased view but define the action method rather than request method
class BandViewset(viewsets.ViewSet):
    def list(self,request):
        bands = Band.objects.all()
        serializer = BandSerializer(bands,many=True)
        return Response(serializer.data,status=200)
    def create(self,request):
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status = 400)


# generic view set  => Either define the action implementation explicitly or use mixins
class GenericBandViewset(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = BandSerializer
    queryset = Band.objects.all()


class ModelBandViewset(viewsets.ModelViewSet):
    serializer_class = BandSerializer
    queryset = Band.objects.all()






    

        
            
            
        
        

 

    
    





