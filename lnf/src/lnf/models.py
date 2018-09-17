from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Admin_Page(models.Model):
    Name = models.CharField(max_length = 30)
    Contact = models.TextField(max_length = 20)
    Lost_Found_Product = models.TextField(max_length = 20)
    Small_Description = models.TextField(max_length = 120)
    Tags = models.CharField(max_length = 50)
    Location = models.TextField()
    Date_and_Time = models.DateTimeField(auto_now = False , auto_now_add = True)
    
    def __str__(self):
    	return self.Name
    def __uicode__(self):
    	return self.Name