from django.urls import path,include
from . import views
from training.views import OrientationTraining
from users.views import RegisterUser,LoginUser
from event.views import EvenNews

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('event/<slug:slug>/', EvenNews.as_view(), name='ev'),
    path('training/<slug:slug>/', OrientationTraining.as_view(), name='tra'),

]
