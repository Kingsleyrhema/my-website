from django.urls import path
from . views import *

app_name='app'
urlpatterns = [
    path('',index, name='index'),
    path('download_cv/', download_cv, name='download_cv'),
]