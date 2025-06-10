from django.db import models



class Vote(models.Model):
	# question_choice = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
	question_id = models.IntegerField()
	date_updated = models.DateTimeField(auto_now_add=True)



