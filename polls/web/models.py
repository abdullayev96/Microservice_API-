from django.db import models



class Poll(models.Model):
	vote = models.FloatField()
	category = models.CharField(max_length=100)

	def __str__(self):
		return self.category



class Author(models.Model):
	full_name = models.CharField(max_length=200, verbose_name="Toliq ismi:")
	bio = models.TextField()
	#image = models.ImageField(upload_to="image/")
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = "Nomzod haqida_"


