from django.db import models

class Jurisdiction(models.Model):
	name = models.CharField(max_length=255, null=False)
	contact = models.ForeignKey("Contact")
	parent_jurisdition = models.ForeignKey("Jurisdiction")

class Contact(models.Model):

	first_name = models.CharField(max_length=255, null=False)
	last_name = models.CharField(max_length=255, null=False)
	email = models.EmailField(null=False)


class Request(models.Model):
	requester_first_name = models.CharField(max_length=255, null=False)
	requester_last_name = models.CharField(max_length=255, null=False)
	requester_email = models.EmailField(max_length=255, null=False)
	text = models.TextField(null=False)
	jurisdiction = models.ManyToManyField("Jurisdiction")
