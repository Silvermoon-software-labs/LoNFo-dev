from __future__ import unicode_literals

from django.db import models
# from taggit.managers import TaggableManager


# Create your models here.

class LostNFound(models.Model):
    Name = models.CharField(max_length=30)
    Contact = models.IntegerField()
    Email = models.EmailField()
    Image = models.ImageField(null=True,
                              blank=True,
                              width_field="width",
                              height_field="height")
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    Lost_Found_Product = models.CharField(max_length=10)
    Small_Description = models.TextField(max_length=120)
    # tags = TaggableManager()
    Location = models.TextField()
    Date_and_Time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Name
