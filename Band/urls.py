from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .serializer import BandSerializer
from .views import BandViewset,GenericBandViewset,ModelBandViewset

router = DefaultRouter()
router.register('Bands',BandViewset,basename='Band')

router1 = DefaultRouter()
router1.register('Bands1',GenericBandViewset,basename='Band1')

router2 = DefaultRouter()
router2.register('Bands2',ModelBandViewset,basename='Band2')

urlpatterns = [
    path('', views.DisplayBands ),
    path('detail/<int:id>/', views.DetailBand ),
    path('class/', views.ClassApi.as_view() ),
    path('classdetail/<int:id>/', views.DetailClassApi.as_view() ),
    path('generic/', views.GenericApi.as_view() ),
    path('generic/<int:id>/', views.DetailGenericApi.as_view() ),
    path('genericmixin/', views.GenericApiMixins.as_view() ),
    path('genericmixin/<int:id>/', views.DetailGenericApiMixins.as_view() ),
    path('viewset/', include(router.urls)),
    path('modelviewset/', include(router2.urls)),
    path('genericviewset/', include(router1.urls)),



]
