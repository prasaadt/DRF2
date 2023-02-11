from django.db import models
from django.contrib import admin

# Create your models here.
class StudentDrf(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

    # def __str__(self):
    #     return self.address

admin.site.register(StudentDrf)