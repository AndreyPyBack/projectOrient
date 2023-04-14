from django.urls import path,include
from . import views


urlpatterns = [
    path('redactor_profile/',views.editor_profile, name='profile'),
    path('event_editing/',views.creating_events,name='event_editing'),
    path('links_editing/',views.creating_link,name='links_editing'),
    path('training_editing/',views.creating_training,name='training_editing'),
    path('delete_comments/',views.creating_comments,name='delete')
]