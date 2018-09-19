from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Admin_Page(models.Model):
    Name = models.CharField(max_length = 30)
    Contact = models.IntegerField()
    # Email = models.EmailField()
    Lost_Found_Product = models.CharField(max_length = 10)
    Small_Description = models.TextField(max_length = 120)
    Tags = ArrayField(models.CharField(max_length=200), blank=True)
    Location = models.TextField()
    Date_and_Time = models.DateTimeField(auto_now = False , auto_now_add = True)
    
    def __str__(self):
    	return self.Name
    def __uicode__(self):
    	return self.Name