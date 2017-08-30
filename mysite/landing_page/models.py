from django.db import models


class Form_Feedback(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	message = models.TextField(max_length=1500)

	def __str__(self):
		return 'from {}'.format(self.name)
