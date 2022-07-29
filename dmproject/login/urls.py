from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('lgin',views.lgin,name='lgin'),
    path('logout',views.logout,name='logout'),
    ]

