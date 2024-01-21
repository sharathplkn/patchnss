from django.urls import path
from . import views

urlpatterns=[
    path('',views.ns,name='ns'),
    path('nss',views.add_volunteer,name='add_volunteer'),
    path("vol",views.view_volunteer,name='view_volunteer'),
    path('rol',views.attendance,name='attendance'),
    path('att',views.view_attendance,name='view_attendance'),
]