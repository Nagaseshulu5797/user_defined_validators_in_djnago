from django.db import models
# Create your models here.
from django.core import validators
class Topic(models.Model):

    
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MinLengthValidator(3)])

class Webpage(models.Model):

    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[validators.MinLengthValidator(3)])
    url=models.URLField()
    email=models.EmailField()
    re_enter_email=models.EmailField()


