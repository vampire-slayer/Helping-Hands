from django.db import models

class Community(models.Model):
	name = models.CharField(max_length=250)
	member = models.CharField(max_length=250)
	logo = models.CharField(max_length=250)

class Members(models.Model):
	community = models.ForeignKey(Community, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	problem = models.CharField(max_length=250)
	image = models.CharField(max_length=250)