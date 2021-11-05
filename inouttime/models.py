from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey 

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now=False, auto_now_add=True) 

    def __str__(self):
        return self.name.username

class Support(models.Model):
    employee = models.ForeignKey(author, on_delete=models.CASCADE)
    support = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.support[:10]



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


class InOutTime(models.Model):
    Intime = models.ForeignKey(Attend, on_delete=models.CASCADE)
    ExitTime = models.ForeignKey(Outtime, on_delete=models.CASCADE)


class EmployeeIP(models.Model):
    ip = models.TextField(default='')
    country = models.TextField(default='')

    def __str__(self):
        return self.ip



