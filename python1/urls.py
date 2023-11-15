from python1.views import *
from django.urls import path
app_name='sr_devloper1'
urlpatterns=[
    path('harshad/',harshad,name='harshad'),
    path('rakesh/',rakesh,name='rakesh'),
]