from django.db import models

class Jurisdiction(models.Model):
	name = models.CharField(max_length=255)
	contact = models.ForeignKey("Contact")
	parent_jurisdition = models.ForeignKey("Jurisdiction")

    

class Contact(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(null=False, blank=False)
