from django.shortcuts import render
from django.views.generic import DetailView
from .models import Training

# Create your views here.
class OrientationTraining(DetailView):
    model = Training
    template_name = 'training/training.html'
    context_object_name = 'orientation_training'