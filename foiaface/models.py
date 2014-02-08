from django.db import models

class Jurisdiction(models.Model):
    name = models.CharField(max_length=255, null=False)
    contact = models.ForeignKey("Contact")
    parent_jurisdiction = models.ForeignKey("Jurisdiction", null=True, blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Request(models.Model):
    requester_first_name = models.CharField(max_length=255, null=False)
    requester_last_name = models.CharField(max_length=255, null=False)
    requester_email = models.EmailField(max_length=255, null=False)
    text = models.TextField(null=False)
    jurisdiction = models.ManyToManyField("Jurisdiction")
    created_at = models.DateTimeField()

    def __str__(self):
        return "Request by %s %s to %s on %s" % (requester_first_name, requester_last_name, jurisdiction, created_at)
