from django.db import models
from django.db.models.deletion import CASCADE

class Note(models.Model):
	name = models.CharField(max_length=255)
	finish_date = models.DateField()
	level = models.IntegerField()
	
class Task(models.Model):
	details = models.CharField(max_length=255)
	priority = models.IntegerField()
	note = models.ForeignKey(Note, on_delete=models.CASCADE)