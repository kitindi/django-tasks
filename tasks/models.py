from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    # created_by = models.ForeignKey(User, related_name='tasks',on_delete=models.CASCADE)
    # updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)
