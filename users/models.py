from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Castom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)