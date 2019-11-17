from django.db import models

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(default=False)
	repository = models.CharField(max_length=200)
	image = models.FilePathField(path="static/img", default=False)
	technology = models.TextField(default=False)

