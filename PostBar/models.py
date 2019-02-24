from django.db import models
import datetime
from django.contrib.auth.models import User

class Category(models.Model):
	title_name = models.CharField(max_length=128, unique=True,primary_key=True)
	class Meta:
		verbose_name_plural = 'Categories'
		
	def __str__(self):  # For Python 2, use __unicode__ too
		return self.title_name
		
	


class Question(models.Model):
	category = models.ForeignKey(Category)
	question_title = models.CharField(max_length=128,primary_key=True)
	question_content = models.CharField(max_length=1000)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	question_isComplete = models.BooleanField(default=False)
	latest_question_published = models.DateField(("Date"), auto_now_add=True)
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):  # For Python 2, use __unicode__ too
		return self.question_title

class Answer(models.Model):
	question_title = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer_id = models.IntegerField(primary_key=True)
	answer_content = models.CharField(max_length=1000)
	answer_username = models.OneToOneField(User,on_delete=models.CASCADE)
	latest_question_published =  models.DateField(("Date"), default=datetime.date.today)
	rank = models.IntegerField(default=0)
	
	def __int__(self):  # For Python 2, use __unicode__ too
		return self.answer_id

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	popular = models.IntegerField(default=0,primary_key=True)
	def __object__(self):  # For Python 2, use __unicode__ too
	   return self.user
	
	
	