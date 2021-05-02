from django.db import models
from django.contrib .auth.models import User


class Advisor(models.Model):
    advisor_name = models.CharField( max_length=50)
    advisor_photoURL = models.URLField(max_length=200)

class booking(models.Model):
    datetime = models.DateTimeField( auto_now=False, auto_now_add=False)
    userid = models.IntegerField(unique=True)
    advisorid = models.IntegerField()
# Create your models here.
