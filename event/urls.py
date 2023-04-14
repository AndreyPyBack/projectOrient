from django.urls import path,include
from . import views


app_name = 'event'
urlpatterns = [
    path('',views.event_list,name='archive'),
]