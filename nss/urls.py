from django.urls import path
from . import views

urlpatterns=[
    path("",views.add_volunteer,name='add_volunteer'),
    path("vol",views.view_volunteer,name='view_volunteer')
]