from django.db import models

class Disease(models.Model):
	data = models.CharField(max_length=25000)
	heading = models.TextField(default =' ')
	key = models.TextField(default =' ')


