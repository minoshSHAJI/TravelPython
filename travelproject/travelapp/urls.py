from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('sachu/',views.sachu,name='sachu'),
    path('mino/',views.mino,name='mino')
]
