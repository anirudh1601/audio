from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Stream(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.CharField(max_length=255)
    password = models.CharField(max_length=200,blank=True)
    date_added = models.DateTimeField(default=datetime.now())
    public_room = models.BooleanField(default=False)
    slug = models.CharField(max_length=244,blank=True)

    def __str__(self):
    	return str(self.room)+' : '+str(self.password)+' : '+str(self.date_added.hour)

    def get_room(self):
    	return str(self.room.all())

    def get_date(self):
    	return str(self.date_added.hour)
    
    def get_absolute_url(self):
        return reverse('dashboard')

