from django.urls import path,include
from . import views


urlpatterns = [
    path('redactor_profile/',views.editor_profile, name='profile'),
    path('event_editing/',views.creating_events,name='event_editing'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('links_editing/',views.creating_link,name='links_editing'),
    path('training_editing/',views.creating_training,name='training_editing'),
    path('delete_comments/',views.creating_comments,name='delete'),
    path('create_event_file_pdf/',views.create_event_file_pdf, name='create_event_file_pdf'),

]