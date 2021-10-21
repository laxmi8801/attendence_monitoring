from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class ApplyLeave(models.Model):
    name = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        d = '{0.startdate} {0.enddate}'
        return d.format(self)



class Time(models.Model):
   name = models.CharField(max_length=50)
   clockin = models.DateField()
   clockout = models.DateField()

   def __str__(self):
       c = '{0.clockin} {0.clockout}'
       return c.format(self)