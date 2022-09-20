from django.urls import path
from .import views
from .views import *


urlpatterns = [
     path('data/',Datas.as_view(),name='details'),
     path('addjobs/',Addjobs.as_view(),name='addjobs'),
     path('checkdata/',Checkdata.as_view(),name='checkdata'),

]
