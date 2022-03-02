
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name="index"),
    path('', views.ListAPIView.as_view(),name="index"),
    #path('create/', views.create,name="create"),
    path('detail/<int:id>', views.DetailAPIView.as_view(),name="detail"),
    path('generic/<int:id>/',views.GenericAPIView.as_view()),
    path('generic/',views.GenericAPIView.as_view()),
]
