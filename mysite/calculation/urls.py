from django.urls import path

from . import views

app_name = 'calculation'
urlpatterns = [
    path('', views.index, name=''),
    ]
