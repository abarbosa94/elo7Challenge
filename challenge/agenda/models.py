from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=42)
	email = models.EmailField(unique=True)

	def __unicode__(self):
		return self.nome

