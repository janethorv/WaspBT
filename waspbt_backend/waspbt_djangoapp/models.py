from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=50)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    