from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=42)
	email = models.EmailField(max_length = 320, unique=True)

	def __unicode__(self):
		return self.name

