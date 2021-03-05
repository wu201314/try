from django.db import models
# Create your models here.
class Fm(models.Model):
	title = models.CharField(max_length=20)
	descipt = models.CharField(max_length=20)
	img = models.FileField(upload_to='')