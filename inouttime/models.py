from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey 

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now=False, auto_now_add=True) 

    def __str__(self):
        return self.name.username

class Intime(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    intime = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Attend(models.Model):
    
    attender = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return str(self.attender.username) + " " + str(self.datetime)[:20]

class Outtime(models.Model):
    
    outtimmer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return str(self.outtimmer.username) + " " + str(self.datetime)[:20]


