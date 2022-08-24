from telnetlib import IP
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=50, null=False)
    slug = models.SlugField()
    description = models.CharField(max_length=255, null=False)
    participants = models.ManyToManyField(User, related_name="participants")
    admins = models.ManyToManyField(User, related_name="admins")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
     

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    slug = models.SlugField
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=400, null=False)
    date = models.DateTimeField(auto_now_add=True)
    
    #Each issue is given a priority, either "low", "medium" or "high"
    LOW_PR = 'LW'
    MED_PR = 'MD'
    HIGH_PR = 'HG'
    
    PRIORITY_CHOICES = [
        (LOW_PR, 'Low'),
        (MED_PR, 'Medium'),
        (HIGH_PR, 'High'),
    ]
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW_PR, blank=True, null=False)
    
    #Each issue is given a state, either "To do", "In progress" or "finished"
    TD_STATE = 'TD'
    IP_STATE = 'IP'
    FI_STATE = 'FI'
    
    STATE_CHOICES = [
        (TD_STATE, 'To do'),
        (IP_STATE, 'In progress'),
        (FI_STATE, 'Finished'),
    ]
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=TD_STATE, blank=True, null=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.project.slug}/{self.slug}' 
    

    
    