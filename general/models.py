from django.db import models

class News(models.Model):
	link = models.CharField(max_length=25000)
	heading = models.TextField(default =' ')
	key = models.TextField(default =' ')
	imagelink = models.TextField(default =' ')

