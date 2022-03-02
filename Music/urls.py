
from django.urls import path,include
from . import views
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .views import ViewsetApi


router = DefaultRouter()
router.register('albums',ViewsetApi,basename='album')

urlpatterns = [
    path('', views.ListAlbum),
    path('detail/<int:pk>/', views.DetailAlbum),
    path('class/', views.AlbumClassApi.as_view(),),
    path('class/detail/<int:pk>', views.DetailAlbumApi.as_view(),),
    path('generic/<int:pk>/', views.GenericApi.as_view()),
    path('generic/', views.GenericApi.as_view()),
    path('viewset/', include(router.urls)),
]
