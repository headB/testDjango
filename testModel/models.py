from django.db import models

# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=20)
    description = models.CharField(max_length=30)