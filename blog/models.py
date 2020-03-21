from django.db import models

# Create your models here.

class Blog(models.Model):
	image = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=1000)
	author = models.CharField(max_length=100)
	datetime = models.DateTimeField(auto_now=True)
	description = models.TextField()
